# ReactorInsight-Dashboard

### A Data-Driven Reactor Performance Analysis Dashboard

---

## Project Overview

**ReactorInsight-Dashboard** is an interactive and dynamic dashboard designed to visualize the performance of different chemical reactors—Batch, Continuous Stirred Tank Reactor (CSTR), and Plug Flow Reactor (PFR)—under various operational conditions (temperature, pressure, catalyst loading, etc.). 

The project leverages Python's powerful data analysis and visualization libraries to help chemical engineers and researchers quickly assess reactor performance, compare between reactor types, and draw meaningful conclusions. It also provides detailed statistical analysis and correlations between reactor parameters.

## Features

- **Interactive Graphs:** Visualizations of reactor performance metrics like temperature vs. conversion and catalyst loading vs. reaction rate.
- **Dynamic Filtering:** Filter the data by reactor type, temperature range, and pressure using an intuitive sidebar.
- **Statistical Summary:** A comprehensive overview of statistical metrics such as mean, median, and standard deviation.
- **Correlation Matrix:** A heatmap to show the relationships between different reactor parameters.
- **Reactor Comparison Tool:** Compare performance metrics between two different reactor types side-by-side.
- **Downloadable Reports:** Users can download filtered data in CSV format for further analysis.
- **User-Friendly Tooltips:** Hover-over explanations to make graphs understandable even for non-experts.

## Technologies Used

- **Python**: The core language for the entire project.
- **Pandas**: For data manipulation and cleaning.
- **Streamlit**: For creating the interactive dashboard.
- **Seaborn & Matplotlib**: For creating the visualizations and correlation matrix.
- **Plotly**: For enhancing the interactivity of the charts and graphs.

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mirdanish6594/ReactorAnalyzer.git
   cd ReactorAnalyzer
2. Create and Activate a Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
3. Install Required Dependencies
   ```bash
   pip install -r requirements.txt
4. Run the Streamlit App
   ```bash
   streamlit run src/dashboard.py
5. Access the App
   The dashboard will open in your web browser at http://localhost:8501

## Usage

1. **Launch the Dashboard**
   - After running the app, the dashboard will automatically open in your web browser.
   - You will see the main interface with options to filter reactor data by type, temperature, and pressure.

2. **Explore the Graphs**
   - Visualize how key parameters such as **temperature**, **conversion rate**, and **reaction rate** vary across different reactor types (Batch, CSTR, PFR).
   - Dynamic graphs will automatically update based on your selected filters.

3. **Comparison Tool**
   - Use the reactor comparison tool to view **side-by-side performance comparisons** between two reactor types.
   - This allows you to compare operating conditions and performance metrics visually.

4. **Download Filtered Data**
   - Click the **Download** button to save filtered reactor data in **CSV** format for offline analysis.
   - You can use this data for further processing or reporting.

## Future Enhancements

Some potential improvements to enhance the functionality of the project:

- **Machine Learning Integration**: Implement predictive models to estimate reactor performance under different operating conditions.
- **Additional Reactors**: Extend the analysis to include other reactor types like packed bed reactors.
- **Real-Time Data**: Stream data from real-world reactors for live performance analysis.
- **User Authentication**: Add user authentication for personalized data views and reports.

## Contributing

If you'd like to contribute to this project:

1. **Fork the repository**.
2. **Create a new feature branch**: 
   ```bash
   git checkout -b feature/new-feature
3. Commit your changes:
   ```bash
   git commit -m 'Add new feature'
4. Push the branch:
   ```bash
   git push origin feature/new-feature
5. Create a Pull Request.
