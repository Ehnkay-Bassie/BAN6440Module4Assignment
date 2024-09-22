# Project Title:  
K-Means Python Application
------------------------------------------

## Project Overview
================
- This project involves constructing a K-Means clustering application to analyze COVID-19 data sourced from the Registry of Open Data on AWS.

---------------------------------------------------

## Project Description
=======================
- The application uses the K-Means algorithm to group regions based on patterns of confirmed cases and death rates. The dataset includes relevant features such as confirmed cases, deaths, and geographic coordinates.

-------------------------------------------------------------------

## Project Instructions
========================
1. **Dataset Selection**: Use the `jhu_csse_covid_19_timeseries_merged.csv` dataset from the [enigma-jhu-timeseries dataset](https://covid19-lake.s3.amazonaws.com/index.html).
2. **Environment Setup**: Ensure Python and the required libraries (`pandas`, `scikit-learn`, `matplotlib`) are installed.
3. **Application Development**: Implement K-Means clustering in `K-meansPythonApp.py`.
4. **Unit Testing**: Run the unit tests provided in `test_kmeans.py` to verify functionality.

----------------------------------------------------------------------------------

## How to Run the Project Files 
===========================
1. Place the dataset in the same directory as the Python files.
2. Execute the main application:
   ```bash
   python K-meansPythonApp.py
------------------------------  

## File Structure
===================
- BAN6440Module4Assignment/
├── K-meansPythonApp.py          # Main application for K-Means clustering
├── test_kmeans.py               # Unit tests for the application
├── jhu_csse_covid_19_timeseries_merged.csv # Dataset used for analysis
└── Executive_Summary.docx       # Executive summary of the project
-------------------------------------

## Conclusion
==========
- The K-Means application successfully clusters regions based on COVID-19 impact, providing valuable insights for health authorities to allocate resources effectively and understand geographic trends.
