let {PythonShell}=require('python-shell')

let pyshell = new PythonShell(__dirname+'\\hey.py');
 
// sends a message to the Python script via stdin

 
pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});

