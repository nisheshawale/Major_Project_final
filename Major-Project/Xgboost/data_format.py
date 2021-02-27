import pandas as pd
from encapsulate import encapsulate_all
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.model_selection import KFold


df = pd.read_excel('data_c.xlsx')
df[['Sim_score', 'ASSR', 'CPMSPC', 'Common_Lines', 'Unused_Variables', 'Unused_Functions']] = df[['First', 'Second']].apply(lambda x: encapsulate_all(x.First, x.Second), axis=1, result_type="expand")
# df['col_3', 'col_4'] = df[['First', 'Second']].apply(lambda x: encapsulate_all(x.First, x.Second), axis=1)
#print(df)
#df.to_csv('data.csv', index = False)
X = df.iloc[:, 3:]
df.plag = pd.Categorical(df.plag)
Y = df.plag.cat.codes
#print(X, Y)


# split data into train and test sets
#seed = 7
test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, stratify=Y)
# fit model no training data
model = XGBClassifier()
#model = svm.SVC()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy without cross validation: %.2f%%" % (accuracy * 100.0))


# KFold Cross Validation approach
kf = KFold(n_splits=4,shuffle=True)
kf.split(X)    
     
# Initialize the accuracy of the models to blank list. The accuracy of each model will be appended to this list
accuracy_model = []
 
# Iterate over each train-test split
for train_index, test_index in kf.split(X):
    # Split train-test
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = Y[train_index], Y[test_index]
    # Train the model
    model = model.fit(X_train, y_train)
    # Append to accuracy_model the accuracy of the model
    accuracy_model.append(accuracy_score(y_test, model.predict(X_test), normalize=True)*100)
 
# Print the accuracy    
print("Accuracy with cross validation: %.2f%%" % (sum(accuracy_model) / len(accuracy_model)))

