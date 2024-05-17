import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import statsmodels.api as smd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import scipy.stats as st
import sklearn
from sklearn.metrics import confusion_matrix
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt 
import seaborn as sns
import sqlite3
from sqlite3 import Error
import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,balanced_accuracy_score,f1_score,precision_score,recall_score,roc_auc_score,confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier


telecom = df = pd.read_csv('telecom.csv')

telecom['TotalCharges'] = telecom['TotalCharges'].replace(' ', np.nan)
telecom['TotalCharges'] = pd.to_numeric(telecom['TotalCharges'])
charge = telecom['MonthlyCharges'] * telecom['tenure']
telecom['TotalCharges'] = charge.where(telecom['TotalCharges'] == np.nan, other=telecom['TotalCharges'])
train,test= train_test_split(telecom, train_size=0.7, test_size=0.3, random_state=100)
train.drop(['customerID'],axis=1,inplace=True)
test.drop(['customerID'],axis=1,inplace=True)

varlist =  ['PhoneService', 'PaperlessBilling', 'Churn', 'Partner', 'Dependents']
def binary_map(x):
    return x.map({'Yes': int(1), "No": 0})
train[varlist] = train[varlist].apply(binary_map)
test[varlist] = test[varlist].apply(binary_map)

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin


class Preprocessor(BaseEstimator, TransformerMixin): 
    # Train our custom preprocessors 
    numerical_columns = [
        
        'tenure','MonthlyCharges','TotalCharges',  
    ]
    
    categorical_columns = [
        'Contract', 'PaymentMethod', 'gender',
        'InternetService', 'MultipleLines', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies',
    ]
    
    
    def fit(self, X, y=None): 

        # Create and fit simple imputer
        self.imputer = SimpleImputer(strategy='median')
        self.imputer.fit(X[self.numerical_columns])
        
        # Create and fit Standard Scaler 
        self.scaler = StandardScaler()
        self.scaler.fit(X[self.numerical_columns]) 
        
        # Create and fit one hot encoder
        self.onehot = OneHotEncoder(handle_unknown='ignore')
        self.onehot.fit(X[self.categorical_columns])
        
        return self 

    def transform(self, X): 
        
        # Apply simple imputer 
        imputed_cols = self.imputer.transform(X[self.numerical_columns])
        onehot_cols = self.onehot.transform(X[self.categorical_columns])
        
        # Copy the df 
        transformed_df = X.copy()
         
        # Apply transformed columns
        transformed_df[self.numerical_columns] = imputed_cols
        transformed_df[self.numerical_columns] = self.scaler.transform(transformed_df[self.numerical_columns])        
        
        # Drop existing categorical columns and replace with one hot equivalent
        transformed_df = transformed_df.drop(self.categorical_columns, axis=1) 
        transformed_df[self.onehot.get_feature_names_out()] = onehot_cols.toarray().astype(int)
        
        return transformed_df
    


rfc = make_pipeline(Preprocessor(), RandomForestClassifier(n_estimators=50))
y_train = train['Churn']
X_train = train.drop('Churn', axis=1)
rfc.fit(X_train, y_train)

params = rfc.get_params()

from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score

y_test = test['Churn']
X_test = test.drop('Churn', axis=1)
y_pred = rfc.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
balanced_accuracy = balanced_accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='binary')
precision = precision_score(y_test, y_pred, average='binary')
recall = recall_score(y_test, y_pred, average='binary')
roc_auc = roc_auc_score(y_test, rfc.predict_proba(X_test)[:, 1])
cm = confusion_matrix(y_test, y_pred)

import mlflow
from mlflow.models import infer_signature

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

# Create a new MLflow Experiment
mlflow.set_experiment("Predict If a Customer Churns")

# Start an MLflow run
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log metrics
    mlflow.log_metric("accuracy_score", accuracy)
    mlflow.log_metric("balanced_accuracy_score", balanced_accuracy)
    mlflow.log_metric("f1_score", f1)
    mlflow.log_metric("precision_score", precision)
    mlflow.log_metric("recall_score", recall)
    mlflow.log_metric("roc_auc_score", roc_auc)
   # mlflow.log_metric("confusion_matrix", cm)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "RandomForestClassifier model for telecom data, n_estimators=50")

    # Infer the model signature
    signature = infer_signature(X_train, rfc.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=rfc,
        artifact_path="classification_model",
        signature=signature,
        input_example=preprocessor.transform(X_train),
        registered_model_name="rfc_model_base_deploy",
    )