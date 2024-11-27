# 🏆 National High School Exam Score Analysis (using HCMC data)

## 📖 Overview
This project is a **Python-based data analysis and visualization tool** designed to analyze the National High School Exam scores using a dataset from **Ho Chi Minh City (HCMC)** for the years 2023 and 2024. The main goal is to process and visualize the data effectively, providing insights into **student performance patterns, statistical distributions,** and trends that can aid educators and policymakers in comparing the two years.

## 📁 Project Structure
The project is organized into several main files and directories:

- **`Main.py`**: 🟢 Initiates data processing and visualization by console for testing functions.
- **`dataProcess/`**: 📂 Contains essential data processing code.
  - **`checkID.py`**: Handles data crawling and processing.
  - **`text.txt`**: Stores intermediate data results.
- **`icon_UI/`**: 🖼 Contains image files for the GUI.
- **`plot/`**: 📊 Contains scripts for creating various plots and visualizations.
  - **`aveSco.py`**: Contains function `plot_average_scores`.
  - **`commonPlot.py`**: Contains functions for various common plots.
  - **`disCompa.py`**: Contains function `plot_student_distribution_comparison`.
  - **`freqSub.py`**: Contains function `freqSub`.
  - **`heatmap.py`**: Contains functions for heatmap visualizations.
  - **`perHis.py`**: Contains function `plot_percentage_histogram`.
- **`utils/`**: 🔧 Contains utility scripts.
  - **`CRUD.py`**:🔄 Handles CRUD operations on CSV data. Provides functions for CRUD (Create, Read, Update, Delete) operations, enabling efficient data management.
- **`UI.py`**: 🖥 Implements a graphical user interface for easy interaction with the dataset.
- **`data/`**: 📋 Contains data files.
  - **`diem2023.csv`**: Contains exam scores for the year 2023.
  - **`diem2024.csv`**: Contains exam scores for the year 2024.

## ✨ Key Features
1. **Data Processing**: 
   - Processes raw exam score data, including converting string data to numeric formats for accurate statistical calculations.
   - Handles missing values and normalizes data entries for consistency.
   - Crawls and processes data from web sources using `checkID.py`.

2. **Data Visualization**: 
   - Generates graphs to visualize data distributions and trends, identifying patterns and anomalies.
   - Outputs statistical summaries to provide insights into the exam scores.
   - Supports various types of plots including histograms, heatmaps, pie charts, and more.

3. **CRUD Functionality**:
   - Allows users to modify the dataset directly from the interface, making it easier to update or correct data as needed.

4. **User Interface (UI)**:
   - A graphical interface to interact with the dataset, display analysis results, and generate visualizations on demand.

## 🚀 How to Use
1. Clone the repository.
2. Run `Main.py` to start the console program.
3. Run `UI.py` to start the program with a graphical user interface.
4. Use the interface to load data, perform CRUD operations, and view visualizations.

## 🔧 Future Work
- Add more data processing features, such as correlation analysis with demographic data.
- Enhance the UI for a better user experience.
- Expand data visualization options for more advanced analysis.
- Optimize data crawling and processing for larger datasets.

## 👥 Contributors
- **Phan Trong Qui (Phanqui72)**: Data processing (Crawling, Collecting, Cleaning, Exporting).
- **Do Kien Hung (darktheDE)**: Data visualization, branch management, project organization using modules and packages.
- **Phan Trong Phu (phantrongphu123)**: UI development, main script functionalities.
- **Tran Thanh Danh (DanhTrannn)**: CRUD mechanism, main script functionalities.
- **Le Dang Khoa (leekhoa0409)**: CRUD mechanism, main script functionalities.

## 📦 Requirements
- **Python 3.x**
- Libraries: `pandas`, `matplotlib`, `seaborn`, `tkinter`

## 🙏 Acknowledgements
This project uses data from the **National High School Exam** and aims to contribute to data-driven educational insights.

Feel free to let me know if you need any further adjustments or additional information!
