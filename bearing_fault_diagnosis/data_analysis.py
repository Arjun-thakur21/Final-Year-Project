import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
import os
from django.conf import settings

def analyze_and_train(df):
    numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
    categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']

    X = df.drop(columns=['Outcome'], axis=1)
    y = df['Outcome']

    num_features = X.select_dtypes(exclude="object").columns
    cat_features = X.select_dtypes(include="object").columns

    numeric_transformer = StandardScaler()
    oh_transformer = OneHotEncoder()

    preprocessor = ColumnTransformer(
        [
            ("OneHotEncoder", oh_transformer, cat_features),
            ("StandardScaler", numeric_transformer, num_features),
        ]
    )
    X = preprocessor.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def evaluate_model(true, predicted):
        mae = mean_absolute_error(true, predicted)
        mse = mean_squared_error(true, predicted)
        rmse = np.sqrt(mean_squared_error(true, predicted))
        r2_square = r2_score(true, predicted)
        accuracy = accuracy_score(true, np.round(predicted)) * 100
        return mae, rmse, r2_square, accuracy

    models = {
        "Linear Regression": LinearRegression(),
        "Ridge": Ridge(),
        "K-Neighbors Regressor": KNeighborsRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest Regressor": RandomForestRegressor(),
        "XGBRegressor": XGBRegressor(),
        "CatBoosting Regressor": CatBoostRegressor(verbose=False),
        "AdaBoost Regressor": AdaBoostRegressor()
    }

    model_list = []
    r2_list = []
    accuracy_list = []
    train_rmse_list = []
    test_rmse_list = []

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        model_train_mae, model_train_rmse, model_train_r2, model_train_accuracy = evaluate_model(y_train, y_train_pred)
        model_test_mae, model_test_rmse, model_test_r2, model_test_accuracy = evaluate_model(y_test, y_test_pred)
        model_list.append(model_name)
        r2_list.append(model_test_r2)
        accuracy_list.append(model_test_accuracy)
        train_rmse_list.append(model_train_rmse)
        test_rmse_list.append(model_test_rmse)

    results_df = pd.DataFrame(list(zip(model_list, r2_list, accuracy_list)), columns=['Model Name', 'R2_Score', 'Accuracy']).sort_values(by=["R2_Score"], ascending=True)

    # Generate HTML table rows
    table_rows = ""
    for index, row in results_df.iterrows():
        table_rows += f"<tr><td>{row['Model Name']}</td><td>{row['R2_Score']:.6f}</td><td>{row['Accuracy']:.2f}</td></tr>"

    # Plot RMSE values
    plt.figure(figsize=(12, 6))  # Increase figure size
    plt.plot(model_list, train_rmse_list, label='Train RMSE')
    plt.plot(model_list, test_rmse_list, label='Test RMSE')
    plt.title('Model RMSE')
    plt.ylabel('RMSE')
    plt.xlabel('Model')
    plt.xticks(rotation=45)  # Rotate x-axis labels
    plt.legend()
    plt.tight_layout()  # Add padding
    plot_save_path = settings.PLOT_SAVE_PATH
    os.makedirs(plot_save_path, exist_ok=True)
    plt.savefig(os.path.join(plot_save_path, 'rmse.png'))

    # Plot accuracy pie chart for overall bearing fault diagnosis
    best_model_index = accuracy_list.index(max(accuracy_list))
    best_model = models[model_list[best_model_index]]
    y_pred = best_model.predict(X_test)
    y_pred_rounded = np.round(y_pred)
    correct_predictions = np.sum(y_test == y_pred_rounded)
    incorrect_predictions = np.sum(y_test != y_pred_rounded)
    labels = ['Correct', 'Incorrect']
    sizes = [correct_predictions, incorrect_predictions]
    colors = ['#4CAF50', '#FF5252']
    explode = (0.1, 0)  # explode the first slice

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Overall Bearing Fault Diagnosis Accuracy')
    plt.tight_layout()
    plt.savefig(os.path.join(plot_save_path, 'bearing_accuracy_pie.png'))

    # Plot accuracy pie chart for each model
    model_accuracies = [accuracy for accuracy in accuracy_list]

    plt.figure(figsize=(6, 6))
    plt.pie(model_accuracies, labels=[f"{model_name}" for model_name in model_list], autopct='%1.1f%%', startangle=140, pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title('Model-wise Bearing Fault Diagnosis Accuracy')
    plt.tight_layout()
    plt.savefig(os.path.join(plot_save_path, 'model_accuracy_pie.png'))

    return table_rows