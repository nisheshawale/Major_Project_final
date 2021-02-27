import os
import pickle
import json
from xgboost import XGBClassifier
import pandas as pd

from encapsulate import encapsulate_all

dir_path = os.path.dirname(os.path.abspath(__file__)) + '/sample_data/'
file_list = os.listdir(dir_path)
total_files = len(file_list)

output = {}
count = 0

if total_files < 2:
    print("Not enough files for comparison")
else:
    for i in range(total_files):
        for j in range(total_files):
            if (i != j) and (i < j):
                features = encapsulate_all(dir_path + file_list[i], dir_path + file_list[j])
                                
                # load model from file
			
                model_path = os.path.dirname(os.path.abspath(__file__))+'/xg.dat'
                print(model_path)
                model = pickle.load(open(model_path, "rb"))

                lists = []
                lists.append(features)
                # make predictions for test data
                data_for_prediction = pd.DataFrame(lists, columns= ['Sim_score', 'ASSR', 'CPMSPC', 'Common_Lines', 'Unused_Variables', 'Unused_Functions'])
                y_pred = model.predict(data_for_prediction)
                # print('---------------------------------')
                # print(y_pred)
                if y_pred[0] == 1:
                    count += 1
                    output[count] = [file_list[i], file_list[j]]

result = json.dumps(output)
# print(result)

# Writing to final_output.json 
with open("final_output.json", "w") as outfile: 
    outfile.write(result) 

