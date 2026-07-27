from dataset_handler import DatasetHandler
from data_analyzer import DataAnalyzer

def main():
    """Main function of the project."""
    file_path = "Dataset/StudentPerformanceFactors.csv"
    dataset = DatasetHandler(file_path)

    dataset.load_data()
    dataset.show_basic_info()

    cleaned_data = dataset.preprocess_data()
    analyzer = DataAnalyzer(cleaned_data)
    analyzer.statistical_summary()
    analyzer.average_score_by_gender()
    analyzer.average_score_by_motivation()
    analyzer.average_score_by_internet()
    analyzer.correlation_analysis()

    analyzer.plot_exam_score_distribution()
    analyzer.plot_gender_comparison()
    analyzer.plot_motivation_comparison()
    analyzer.plot_hours_vs_score()
    analyzer.plot_attendance_line_chart()
    analyzer.plot_exam_score_correlation_bar()

if __name__ == "__main__":
    main()


