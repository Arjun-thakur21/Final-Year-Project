# Code Citations

## License: unknown
https://github.com/IhorKim/mlproject/tree/f87aba5bda508de45112a4876f6a3d4f60dbad0c/notebook/MODEL_TRAINING.py

```
"object").columns
       cat_features = X.select_dtypes(include="object").columns

       numeric_transformer = StandardScaler()
       oh_transformer = OneHotEncoder()

       preprocessor = ColumnTransformer(
           [
               ("OneHotEncoder", oh_transformer, cat_features),
               ("StandardScaler", numeric_transformer, num_features),
```


## License: unknown
https://github.com/mallana2019/student-CML-GITHUB/tree/f3357f73a58443b79a1f16a933b8e6fab0e10184/train.py

```
select_dtypes(exclude="object").columns
       cat_features = X.select_dtypes(include="object").columns

       numeric_transformer = StandardScaler()
       oh_transformer = OneHotEncoder()

       preprocessor = ColumnTransformer(
           [
               ("OneHotEncoder", oh_transformer, cat_features),
               ("StandardScaler", numeric_transformer
```


## License: unknown
https://github.com/SrijanDeo-DA-DS/Regression---DataScience_Job_Salary_Predictor/tree/e248e935a506fe767bed79805a3cdc9f5f7db3d7/src/components/model_trainer.py

```
= train_test_split(X, y, test_size=0.2, random_state=42)

       def evaluate_model(true, predicted):
           mae = mean_absolute_error(true, predicted)
           mse = mean_squared_error(true, predicted)
           rmse = np.sqrt(mean_squared_error(true, predicted))
           r2_square
```


## License: unknown
https://github.com/EfthimiosVlahos/Student-Performance-End-to-End-ML-Project/tree/13a9c912bcb0d97888f34ded4e5679b50ea286d5/README.md

```
def evaluate_model(true, predicted):
           mae = mean_absolute_error(true, predicted)
           mse = mean_squared_error(true, predicted)
           rmse = np.sqrt(mean_squared_error(true, predicted))
           r2_square = r2_score(true, predicted)
           return mae, rmse, r2_square

       models = {
           "
```


## License: Apache_2_0
https://github.com/malleswarigelli/Deploy_MLmodel_AWS_EC2/tree/20e8bf7030e4d2deb065b4eb0f55af2189d800ce/src/utils.py

```
(),
           "Ridge": Ridge(),
           "K-Neighbors Regressor": KNeighborsRegressor(),
           "Decision Tree": DecisionTreeRegressor(),
           "Random Forest Regressor": RandomForestRegressor(),
           "XGBRegressor": XGBRegressor(),
           "CatBoosting Regressor": CatBoostRegressor
```

