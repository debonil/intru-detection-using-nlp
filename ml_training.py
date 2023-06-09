# -*- coding: utf-8 -*-
"""Ravi_Trying.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pD4wo69Jftyk42j8kSzrQitHJfcUMueX
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report,roc_auc_score,auc,f1_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Read the training CSV file containing normal traffic data
df_normal_train = pd.read_csv('data/processed/train_normal.csv')

# Read the testing CSV file containing abnormal traffic data
df_test_abnormal = pd.read_csv('data/processed/test_abnormal.csv')

# Read the testing CSV file containing normal traffic data
df_test_normal = pd.read_csv('data/processed/test_normal.csv')

df_concat = pd.concat([df_normal_train, df_test_abnormal, df_test_normal])

# Shuffle the concatenated dataframe
df_shuffled = df_concat.sample(frac=1, random_state=42)

df_shuffled.groupby("label").count()

vectorizer = CountVectorizer(max_features=2000)
vectorizer.fit(df_shuffled['request'])
dictionary = vectorizer.vocabulary_

# Convert HTTP requests to feature vectors
x_train_normal = vectorizer.transform(df_shuffled['request']).toarray()
y_train_normal = df_shuffled['label']

print(x_train_normal.shape)

# Split the shuffled dataset into training and testing sets


x_train, x_test, y_train, y_test = train_test_split(
    x_train_normal, y_train_normal, test_size=0.2, random_state=42)

models = {"Decision Tree": DecisionTreeClassifier(random_state=42),
          "Random Forest": RandomForestClassifier(random_state=42),
          "Ensmb Decision Tree": BaggingClassifier(estimator=DecisionTreeClassifier(random_state=42), n_estimators=5),
          "Ensmb Random Forest": BaggingClassifier(estimator=RandomForestClassifier(random_state=42), n_estimators=5),
          "Naive Bayes": MultinomialNB(),
          "Neural Net": MLPClassifier(hidden_layer_sizes=[2048, 1024]),
          "Ensmb Naive Bayes": BaggingClassifier(estimator=MultinomialNB(), n_estimators=5),
          "Ensmb Neural Net": BaggingClassifier(estimator= MLPClassifier(hidden_layer_sizes=[2048, 1024]), n_estimators=5),
          "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression()),
          "Ensmb Logistic Regression": BaggingClassifier(estimator= make_pipeline(StandardScaler(), LogisticRegression()), n_estimators=5),
          "Support Vector Machine": SVC(),
          "Ensmb SVM": BaggingClassifier(estimator=SVC(), n_estimators=5),
          }

import time
results = []
results_df = []

for name, model in models.items():
    start = time.time()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)
    print(f"{name} accuracy on abnormal traffic data: {accuracy}")
    print(f"{name} F1 on normal traffic data: {f1}")
    print(f"{name} roc_auc on normal traffic data: {roc_auc}")
    results.append({
        "model":name,
        "accuracy":accuracy,
        "f1_score":f1,
        "roc_auc":roc_auc,
        "time":(time.time()-start)/1000,
    })
    results_df=pd.DataFrame(results)
    results_df.to_csv('final_result.csv', index=False)

results_df