import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectFromModel

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()  # Clean column names

    # Check if 'Disease' column exists
    if 'Disease' not in df.columns:
        raise KeyError("Column 'Disease' not found in dataset.")

    # Create a new feature: SymptomSeverity
    df['SymptomSeverity'] = df['Symptoms/Condition'].apply(lambda x: len(x.split()))

    # Separate features and target
    X = df.drop('Disease', axis=1)
    y = df['Disease']

    # Define numerical and categorical columns
    numerical_cols = ['Dosage (mg)', 'SymptomSeverity']
    categorical_cols = [col for col in X.columns if col not in numerical_cols]

    # Create preprocessing pipelines
    numerical_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    # Apply transformations
    X_preprocessed = preprocessor.fit_transform(X)

    return X_preprocessed, y

from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def train_random_forest(X_train, y_train):
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'criterion': ['gini', 'entropy'],
        'max_features': ['auto', 'sqrt', 'log2']
    }

    rf = RandomForestClassifier(random_state=42)
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    print(f"Best Parameters: {grid_search.best_params_}")

    return grid_search.best_estimator_

# Function to evaluate the model
def evaluate_model(model, X_val, y_val, dataset_type="Validation"):
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)

    print(f"{dataset_type} Accuracy: {accuracy * 100:.2f}%")
    print(f"{dataset_type} Classification Report:")
    print(report)

    return accuracy, report

# Function to display feature importance
def display_feature_importance(model, feature_names):
    importances = model.feature_importances_
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    print(feature_importance_df.sort_values(by='Importance', ascending=False))

def random_forest_with_regularization(
    data_path, target_column, test_size=0.2, cv_folds=5,
    n_estimators=100, max_depth=10, min_samples_split=10,
    min_samples_leaf=4, random_state=42
):
    """
    Trains a Random Forest model with regularization and cross-validation.
    """
    # Load and preprocess the dataset
    X, y = load_and_preprocess_data(data_path)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Initialize the Random Forest Classifier with regularization parameters
    rf_classifier = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        random_state=random_state
    )

    # Perform cross-validation
    cv_scores = cross_val_score(
        rf_classifier, X_train, y_train, cv=cv_folds
    )
    cv_accuracy = cv_scores.mean() * 100

    # Train the model
    rf_classifier.fit(X_train, y_train)

    # Evaluate the model on the test set
    y_pred = rf_classifier.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred) * 100
    classification_rep = classification_report(y_test, y_pred, output_dict=True)

    # Prepare results
    results = {
        'cv_accuracy': cv_accuracy,
        'test_accuracy': test_accuracy,
        'classification_report': classification_rep
    }

    return results

# Main execution function to handle everything
def main():
    # File paths of the datasets
    train_file_path = 'synthetic_detailed_ayurveda_dataset.csv'  # Detailed dataset for training
    test_file_path = 'synthetic_ayurveda_dataset.csv'  # Simpler dataset for validation/testing

    # Step 1: Load and preprocess both datasets
    df_train = load_and_preprocess_data(train_file_path)
    df_test = load_and_preprocess_data(test_file_path)

    # Step 2: Split data (training from detailed, testing from simpler dataset)
    X_train, X_test, y_train, y_test = split_data(df_train, df_test, target_column='Disease')

    # Step 3: Train Random Forest model using the training dataset
    rf_classifier = train_random_forest(X_train, y_train)

    # Step 4: Evaluate the model on the validation/test dataset
    evaluate_model(rf_classifier, X_test, y_test)

    # Step 5: Display feature importance from the trained model
    display_feature_importance(rf_classifier, X_train.columns)

if __name__ == "__main__":
    main()