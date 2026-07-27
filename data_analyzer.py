import numpy as np
import matplotlib.pyplot as plt

class DataAnalyzer:
    """Performs analysis and visualization."""
    def __init__(self,data):
        self.data = data

    def statistical_summary(self):
        """Show statistical summary"""
        print("\nStatistical summary")
        print(self.data.describe())

    def average_score_by_gender(self):
        """Show average exam score by gender."""
        result = self.data.groupby("Gender")["Exam_Score"].mean()
        print("\nAverage Exam Score by Gender:")
        print(result)


    def average_score_by_motivation(self):
        """Show average exam score by motivation level."""
        result = self.data.groupby("Motivation_Level")["Exam_Score"].mean()

        print("\nAverage Exam Score by Motivation Level:")
        print(result)

    def average_score_by_internet(self):
        """Show average exam score by internet access."""
        result = self.data.groupby("Internet_Access")["Exam_Score"].mean()

        print("\nAverage Exam Score by Internet Access:")
        print(result)


    def correlation_analysis(self):
        """Show correlation between numerical columns and exam score."""
        selected_columns = [
            "Hours_Studied",
            "Attendance",
            "Sleep_Hours",
            "Previous_Scores",
            "Tutoring_Sessions",
            "Physical_Activity",
            "Exam_Score"
        ]
        correlation = self.data[selected_columns].corr()

        print("\nCorrelation with Exam Score:")
        print(correlation["Exam_Score"].sort_values(ascending=False))


    def plot_exam_score_distribution(self):
        """Create histogram of exam scores with median line."""
        median_score = np.median(self.data["Exam_Score"])
        plt.figure(figsize=(9, 5))
        plt.hist(self.data["Exam_Score"],
            bins=15,
            color="#7FB3D5",
            edgecolor="black")

        plt.axvline(median_score,
                    color="red",
                    linestyle="--",
                    linewidth=2,
                    label=f"Median = {median_score:.1f}")

        plt.title("Distribution of Exam Scores")
        plt.xlabel("Exam Score")
        plt.ylabel("Number of Students")
        plt.xlim(0, 100)
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()



    def plot_gender_comparison(self):
        """Create bar chart of average exam score by gender."""
        result = self.data.groupby("Gender")["Exam_Score"].mean()
        median_score = np.median(self.data["Exam_Score"])

        plt.figure(figsize=(7, 5))
        plt.bar(result.index,
            result.values,
            color=["#F5B7B1", "#85C1E9"],
            edgecolor="black")

        plt.axhline(median_score,
                    color="red",
                    linestyle="--",
                    linewidth=2,
                    label=f"Median = {median_score:.1f}")

        plt.title("Average Exam Score by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Average Exam Score")
        plt.ylim(0, 100)
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()



    def plot_motivation_comparison(self):
        """Create bar chart of average score by motivation level."""
        result = self.data.groupby(["Motivation_Level"])["Exam_Score"].mean()
        median_score = np.median(self.data["Exam_Score"])

        plt.figure(figsize=(8, 5))
        plt.bar(
            result.index,
            result.values,
            color="#A9DFBF",
            edgecolor="black")

        plt.axhline(
            median_score,
            color = "red",
            linestyle = "--",
            linewidth=2,
            label=f"Median = {median_score:.1f}")

        plt.title("Average Exam Score by Motivation Level")
        plt.xlabel("Motivation Level")
        plt.ylabel("Average Exam Score")
        plt.ylim(0, 100)
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()


    def plot_hours_vs_score(self):
        """Create scatter plot of study hours and exam score."""
        median_score = np.median(self.data["Exam_Score"])

        plt.figure(figsize=(9, 5))
        plt.scatter(self.data["Hours_Studied"],
            self.data["Exam_Score"],
            color="#AF7AC5",
            alpha=0.6,
            edgecolor="black")
        plt.axhline(median_score,
            color="red",
            linestyle = "--",
            linewidth=2,
            label=f"Median = {median_score:.1f}")
        plt.title("Hours Studied vs Exam Score")
        plt.xlabel("Hours Studied")
        plt.ylabel("Exam Score")
        plt.ylim(0, 100)
        plt.legend()
        plt.grid(linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()



    def plot_attendance_line_chart(self):
        """Create line chart of average exam score by attendance range."""
        attendance_groups = self.data.copy()

        attendance_groups["Attendance_Group"] = (attendance_groups["Attendance"] // 10 * 10)

        result = attendance_groups.groupby("Attendance_Group")["Exam_Score"].mean()
        median_score = np.median(self.data["Exam_Score"])

        plt.figure(figsize=(9, 5))
        plt.plot(result.index,
            result.values,
            marker="o",
            color="#2E86C1",
            linewidth=2)

        plt.axhline(median_score,
            color = "red",
            linestyle = "--",
            linewidth=2,
            label=f"Median = {median_score:.1f}")

        plt.title("Average Exam Score by Attendance Range")
        plt.xlabel("Attendance Range")
        plt.ylabel("Average Exam Score")
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        plt.legend()
        plt.grid(linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

    def plot_exam_score_correlation_bar(self):
        """Create horizontal bar chart of correlations with exam score."""
        selected_columns = [
            "Hours_Studied",
            "Attendance",
            "Sleep_Hours",
            "Previous_Scores",
            "Tutoring_Sessions",
            "Physical_Activity"]

        correlations = self.data[selected_columns + ["Exam_Score"]].corr()
        exam_score_corr = correlations["Exam_Score"].drop("Exam_Score")
        exam_score_corr = exam_score_corr.sort_values()

        plt.figure(figsize=(9, 5))
        plt.barh(
            exam_score_corr.index,
            exam_score_corr.values,
            color="#76D7C4",
            edgecolor="black")

        plt.axvline(
            0,
            color="black",
            linewidth=1)

        plt.title("Correlation of Factors with Exam Score")
        plt.xlabel("Correlation Value")
        plt.ylabel("Factors")
        plt.xlim(-1, 1)
        plt.grid(axis="x", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()