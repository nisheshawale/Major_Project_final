const express=require('express');
const bodyParser=require('body-parser')
const path = require('path');
const fs=require('fs');
const multer=require('multer');
const { json } = require('body-parser');
let {PythonShell}=require('python-shell')
let cors=require('cors');


let port = process.env.PORT;
const app=express()

app.use(bodyParser.json())//This is used for parsing the json information so that the api undestands 
//the json object that is sent to it!

app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));


const storage = multer.memoryStorage();
const upload = multer({ storage: storage });
app.get('/',(req,res)=>{
    res.send('hey')
})
app.get('/checkCodePlag',(req,res)=>{
    
    let code_path=path.resolve(__dirname+'/../../Xgboost/');
    let pyshell = new PythonShell(code_path+'/script.py');
 
    // sends a message to the Python script via stdin
    
     
    pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      console.log(message);
    });
     
    // end the input stream and allow the process to exit
    pyshell.end(function (err,code,signal) {
      if (err) throw err;
      fs.readFile(path.resolve(code_path+'/final_output.json'), 'utf8', function (err,data) {
        if (err) {
          return console.log(err);
        }
        console.log(data);
        res.send(JSON.parse(data))
      });
    });
    

    
})

app.get('/checkTextPlag',(req,res)=>{
    
  console.log("Script calling started")
  let code_path=path.resolve(__dirname+'/../../Text Similarity/text_alignment/');
  let pyshell = new PythonShell(code_path+'/main.py');

  // sends a message to the Python script via stdin
  
   
  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
  });
   
  // end the input stream and allow the process to exit
  pyshell.end(function (err,code,signal) {
    if (err) throw err;
    fs.readFile(path.resolve(code_path+'/final_output.json'), 'utf8', function (err,data) {
      if (err) {
        return console.log(err);
      }
      console.log(data);
      res.send(JSON.parse(data))
    });
  });
  

  
})

app.post('/uploadCode',upload.single("myFile"),(req,res,next) => {
    console.log(req.file.originalname)
    const file=req.file;
    if (!file) { // in case we do not get a file we return
      const error = new Error("Please upload a file");
      error.httpStatusCode = 400;
      return next(error);
    }
    const multerText = Buffer.from(file.buffer).toString("utf-8"); 
    fs.writeFile(path.resolve(`./../../Major-Project/Xgboost/sample_data/${req.file.originalname}`),multerText,(err)=>{
      if (err){
        console.log(err)
      }else{
        console.log("file written successfully")
      }
    })
    res.send(multerText);

})

app.post('/uploadText',upload.single("myFile"),(req,res,next) => {
  console.log(req.file.originalname)
  const file=req.file;
  if (!file) { // in case we do not get a file we return
    const error = new Error("Please upload a file");
    error.httpStatusCode = 400;
    return next(error);
  }
  const multerText = Buffer.from(file.buffer).toString("utf-8"); 
  fs.writeFile(path.resolve(`./../../Major-Project/Text Similarity/text_alignment/files/${req.file.originalname}`),multerText,(err)=>{
    if (err){
      console.log(err)
    }else{
      console.log("file written successfully")
    }
  })
  res.send(multerText);

})


if (port == null || port == "") {
    port = 8000;
  }
app.listen(port,()=>{
    console.log("Listening on port 8000")
})
