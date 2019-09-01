import tensorflow as tf
from tensorflow import keras

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pickle

import pandas as pd

class PredictingManager:
    def __init__(self):
        self.model = keras.models.load_model("my_keras_model.h5")
        self.num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy="mean")),
            ('std_scaler', StandardScaler()),
        ])
        self.num_attribs = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
        self.cat_attribs = ['Sex', 'Embarked']

        filename = '/app/full_pipeline.pkl'
        #filename = 'full_pipeline.pkl'
        with open(filename, 'rb') as f:
            self.full_pipeline = pickle.load(f)


    def do_predict(self,data):
        data = [[data['passengerClass'], data['age'], data['sibSp'], data['parCh'], data['fare'], data['sex'], data['embarked']]]
        df = pd.DataFrame(data, columns=['Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex', 'Embarked'])
        print(df.head())
        X_data_prepared = self.full_pipeline.transform(df)
        print(X_data_prepared)
        predicted_class = self.model.predict_classes(X_data_prepared)
        predicted_prob = self.model.predict(X_data_prepared)
        predicted_class_str = str(predicted_class[0][0])
        predicted_prob_str = str(round(predicted_prob[0][0] * 100))
        print(predicted_class_str)
        print(predicted_prob_str)
        predict_data = [predicted_class_str, predicted_prob_str]
        return predict_data