import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import urllib.request

# Download the data
def download_data():
    url = "https://www.spc.noaa.gov/wcm/data/"
    years = range(2000, 2022)
    for year in years:
        file_name = f"torn{year}.csv.gz"
        urllib.request.urlretrieve(url + file_name, file_name)

# Load and preprocess the data
def load_data():
    years = range(2000, 2022)
    data_frames = []

    for year in years:
        file_name = f"torn{year}.csv.gz"
        df = pd.read_csv(file_name, compression='gzip')
        data_frames.append(df)

    data = pd.concat(data_frames, ignore_index=True)
    return preprocess_data(data)

# Preprocess the data
def preprocess_data(data):
    # Select relevant features
    data = data[['yr', 'mo', 'dy', 'date', 'time', 'tz', 'st', 'mag', 'inj', 'fat', 'loss', 'slat', 'slon', 'elat', 'elon']]

    # Create the target variable: 1 for tornadoes with intensity EF2 and above, 0 for EF0 and EF1
    data['intense_tornado'] = np.where(data['mag'] >= 2, 1, 0)

    # Drop unnecessary columns
    data.drop(['yr', 'mo', 'dy', 'date', 'time', 'tz', 'st', 'mag'], axis=1, inplace=True)

    # Drop rows with missing values
    data.dropna(inplace=True)

    # Split the data into features (X) and target (y)
    X = data.drop('intense_tornado', axis=1)
    y = data['intense_tornado']

    return X, y

# Feature engineering
def feature_engineering(X):
    # Standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled

# Train the random forest classifier on the data
def train_rf_classifier(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the classifier with default parameters
    clf = RandomForestClassifier(random_state=42)

    # Perform grid search for hyperparameter tuning
    param_grid = {
        'n_estimators': [100, 200, 500],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False]
    }

    grid
