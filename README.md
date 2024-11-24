# Data and Information Quality Project: Milano Services Dataset

This repository contains the work done for the **Data and Information Quality** project, where we analyze and clean a dataset related to services in Milan, specifically focusing on hairdressers and beauticians. The dataset has been sourced from the Italian open data platform **Comune di Milano**. The project aims to apply data quality techniques, such as data profiling, cleaning, and analysis, to this real-world dataset.

### Project Overview

The dataset contains information on commercial activities, specifically focusing on services like hairdressing and beauty services in Milan. This data will be cleaned, processed, and analyzed through the following pipeline:

1. **Data Profiling**: Investigating the dataset's characteristics, missing values, and potential issues.
2. **Data Cleaning**:
   - **Transformation & Standardization**: Formatting and ensuring consistency across data columns.
   - **Error Detection & Correction**: Handling missing values and potential outliers.
   - **Deduplication**: Identifying and removing duplicates to ensure data quality.
3. **Data Analysis** : Performing a suitable analysis (e.g., clustering, classification, regression) on both the raw and cleaned datasets. (to modify)

### Repo Structure

The project repository is structured as follows:

```
/project-directory │ ├── notebooks/ # Jupyter Notebooks for analysis and exploration │ ├── 01-first-logical-notebook.ipynb │ ├── 02-second-logical-notebook.ipynb │ └── prototype-notebook.ipynb │ ├── src/ # Source code for the project │ ├── init.py │ ├── data_preparation.py # Data cleaning and transformation functions │ ├── data_analysis.py # Data analysis and model-related functions │ └── utils.py # Helper functions │ ├── data/ # Raw, processed, and cleaned data │ ├── raw/ # Raw data as provided by Comune di Milano │ ├── processed/ # Intermediate processed data │ └── cleaned/ # Final cleaned dataset │ ├── tests/ # Unit tests to ensure code correctness │ ├── test_data_preparation.py │ └── test_data_analysis.py │ ├── requirements.txt # Required Python libraries for the project ├── .gitignore # Files and directories to be excluded from version control ├── README.md # Project documentation └── environment.yml # Conda environment file (if using Conda)
```

### How to Use This Repository

1. **Clone the repository**:

   Run the following command to clone the repository to your local machine:
   ```bash git clone https://github.com/your-username/your-repo-name.git

2. **Set up the environment**:

   Install dependencies via pip:
   ```pip install -r requirements.txt

### Collaborators

This project is a collaborative effort between:

- **Mauro Orazio Drago** (Project Lead)
- **Dennis Pierantozzi**
- **Davide Morelli**

Each team member contributed to different aspects of the project, including data cleaning, analysis, and report generation. The collaboration ensures that each component of the project meets the necessary requirements and produces high-quality results.
