# Imports
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import pickle


def train_model():
    # Load data
    train = pd.read_csv('data/raw/diamonds_train.csv')
    test = pd.read_csv('data/raw/diamonds_test.csv')
    full = pd.read_csv('data/raw/diamonds.csv')

    # Identify columns
    NUM_FEATS = ['x', 'y', 'z', 'depth', 'table', 'carat']
    CAT_FEATS = ['cut', 'color', 'clarity']
    ALL_FEATS = NUM_FEATS + CAT_FEATS
    TARGET = 'price'

    # Split the data into train and test subsets
    X_train, X_test = train_test_split(train, test_size=0.10)
    print(X_train.shape)
    print(X_test.shape)

    # transformer. Improve model accuracy by enhancing data
    transformer = ColumnTransformer(transformers=[("scaler", RobustScaler(), NUM_FEATS),
                                                  ("encoder", OneHotEncoder(), CAT_FEATS)])

    # Set the pipeline, transformer and model: Random Forest Regressor
    pipe = Pipeline(steps=[("transformer", transformer),
                           ("model", RandomForestRegressor(n_estimators=512, max_depth=16))], verbose=10)

    # Training the model using pipeline
    df_to_use = full
    pipe.fit(df_to_use[ALL_FEATS], df_to_use[TARGET])
    print("Model trained")

    # Predicting our y_test using X_test previously split
    y_test = pipe.predict(X_test[ALL_FEATS])
    y_train = pipe.predict(X_train[ALL_FEATS])
    # Calculate rmse for both, test and train previously split
    rmse_test = mean_squared_error(y_pred=y_test, y_true=X_test[TARGET], squared=False)
    rmse_train = mean_squared_error(y_pred=y_train, y_true=X_train[TARGET], squared=False)
    # Calculate r squared for both, test and train previously split
    r2_test = r2_score(y_pred=y_test, y_true=X_test[TARGET])
    r2_train = r2_score(y_pred=y_train, y_true=X_train[TARGET])
    print(f"rmse test error: {rmse_test}")
    print(f"rmse train error: {rmse_train}")
    print(f"r2 test error: {r2_test}")
    print(f"r2 train error: {r2_train}")

    # Predicting new data
    # y_new_data = pipe.predict(test[ALL_FEATS])

    # Saving model into a binary file
    binary_path = "data/model_binary/"
    binary_name = "RandomForest.pkl"
    with open(f'{binary_path}{binary_name}', "wb") as f:
        pickle.dump(pipe, f)

    print(f"Model saved at the following path: {binary_path}{binary_name}")


train_model()
