# Naive Bayes Classifier from Scratch
This project implements a Naive Bayes Classifier from scratch using Python. The classifier is used to classify mushrooms as either edible or poisonous based on various features such as cap shape, cap color, gill color, etc.

## Getting Started
To use this classifier, you will need Python 3 installed on your computer. You will also need the following libraries:

- numpy
- pandas

To install these libraries, run the following command:

``` bash
pip install numpy pandas
```

## Usage
To use this classifier, you first need to have a dataset in the form of a CSV file with columns representing the features and a column for the class (edible or poisonous). This project includes a sample dataset (`Mushroom_Train.csv` and `Mushroom_Test.csv`) that can be used for testing.

1. Load the dataset using pandas:
``` python
import pandas as pd

df = pd.read_csv('./Mushroom_Train.csv')
```

2. Preprocess the dataset by encoding the categorical features:
``` python
from naive_bayes import encodeCol

obj_df = df.select_dtypes(include=['object']).copy()
obj_df["stalk-root"].replace({"?": "b"}, inplace=True)

encoded_all = {}
for col in obj_df.columns:
    encoded_all[col] = encodeCol(obj_df[col])
    
df_train = obj_df.replace(encoded_all)
```

3. Split the dataset into features and class:
``` python
X_train = df_train.drop('class', axis=1)
y_train = df_train['class']
```

4. Train the classifier:
``` python
from naive_bayes import GNaiveBayesClassifier

model = GNaiveBayesClassifier()
model.train(X_train, y_train)
```

5. Load the test dataset and preprocess it the same way as the training dataset:
``` python
df_test = pd.read_csv('./Mushroom_Test.csv')
df_test["stalk-root"].replace({"?": "b"}, inplace=True)

encoded_all = {}
for col in df_test.columns:
    encoded_all[col] = encodeCol(df_test[col])
    
df_test = df_test.replace(encoded_all)

X_test = df_test.drop('class', axis=1)
y_test = df_test['class']
```

6. Make predictions on the test dataset:
``` python
predicted = model.predict(X_test)
```

7. Evaluate the performance of the classifier using accuracy and confusion matrix:
``` python 
accuracy = model.accuracy(y_test, predicted)
confusion_matrix = model.confusionMatrix(predicted, y_test)
```

## Naive Bayes Classifier
Naive Bayes is a classification algorithm based on Bayes' theorem. It assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature. This is called the "naive" assumption, hence the name Naive Bayes.

Naive Bayes calculates the probability of each class given the input features and selects the class with the highest probability as the output.

The algorithm consists of two steps: training and prediction. During training, the model learns the probability distribution of each feature given each class. During prediction, the model calculates the probability of each class given the input features using Bayes' theorem and selects the class with the highest probability as the output.

