import numpy as np
import pandas as pd

class DatasetHandler:
    """Handles loading and preprocessing of the dataset."""
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load dataset from CSV file."""
        self.data = pd.read_csv(self.file_path)
        print("Dataset loaded successfully.")
        return self.data

    def show_basic_info(self):
        """Show basic information about the dataset."""
        print("\nFirst 5 rows:")
        print(self.data.head())

        print("\nDataset shape:")
        print(self.data.shape)

        print("n\Column names:")
        print(self.data.columns.tolist())

        print("\nDataset info:")
        print(self.data.info())


    def create_missing_values(self):
        """Create missing values for showing preprocess."""
        self.data.loc[5,"Hours_Studied"] = np.nan
        self.data.loc[10, "Attendance"] = np.nan
        self.data.loc[20, "Sleep_Hours"] = np.nan
        self.data.loc[30, "Previous_Scores"] = np.nan

        print("\nArtificial missing values were created.")


    def check_missing_values(self):
        """Check missing values in the dataset."""
        print("\nMissing values after cleaning:")
        print(self.data.isnull().sum())


    def handle_missing_values(self):
        """Fill missing values using median/mode."""
        numeric_columns = self.data.select_dtypes(
            include =  [np.number]).columns
        for column in numeric_columns:
            median_value = np.median(self.data[column].dropna())
            self.data[column] = self.data[column].fillna(median_value)

        categorical_columns = self.data.select_dtypes(
            include = ["object"]).columns

        for column in categorical_columns:
            mode_value = self.data[column].mode()[0]
            self.data[column] = self.data[column].fillna(mode_value)
        print("\nMissing values handled successfully")


    def remove_duplicates(self):
        """Remove duplicate rows from the dataset."""
        before = len(self.data)
        self.data = self.data.drop_duplicates()
        after = len(self.data)
        print(f"\nRemoved duplicates: {before - after}")


    def add_score_level_column(self):
        """Add score level column based on exam score."""
        self.data["Score_level"] = np.where(
            self.data["Exam_Score"] >= 75,
            "High",
            "Low/Medium")


    def add_study_hours_group(self):
        """Add study hours group column."""
        self.data["Study_Hours_Group"] = pd.cut(
            self.data["Hours_Studied"],
            bins=[0, 10, 20, 30, 40, 100],
            labels = ["0-10", "11-20", "21-30", "31-40", "40+"])

    def preprocess_data(self):
        """Run the full preprocessing process."""
        self.create_missing_values()
        self.check_missing_values()
        self.handle_missing_values()
        self.remove_duplicates()
        self.add_score_level_column()
        self.add_study_hours_group()

        print("\nMissing values after cleaning:")
        print(self.data.isnull().sum())
        print("\nPreprocessing completed successfully.")
        return self.data
    def get_data(self):
        """Return cleaned dataset."""
        return self.data