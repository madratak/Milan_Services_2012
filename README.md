<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/it/b/be/Logo_Politecnico_Milano.png" width="300"/>
</p>

# DIQ Project

This repository contains the work done for the **Data and Information Quality** project at **PoliMI**, where we analyze and clean a dataset related to services in Milan, specifically focusing on hairdressers and beauticians. The project aims to apply data quality techniques, such as data profiling, cleaning, and analysis, to this real-world dataset.

The dataset has been sourced from the Italian open data platform of the *Comune di Milano* ([link](http://www.datiopen.it/it/opendata/Comune_di_Milano_Esercizi_commerciali_Servizi_alla_persona_parrucchieri_estetisti_
)).

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
/project-directory
│
├── notebooks/                  # Jupyter Notebooks for analysis and exploration
│   ├── 01-first-logical-notebook.ipynb
│   └── prototype-notebook.ipynb
│
├── src/                        # Source code for the project
│   ├── data_preparation.py     # Data cleaning and transformation functions
│   ├── data_analysis.py        # Data analysis and model-related functions
│   └── utils.py                # Helper functions
│
├── data/                       # Raw, processed, and cleaned data
│   ├── raw/                    # Raw data as provided by Comune di Milano
│   ├── processed/              # Intermediate processed data
│   └── cleaned/                # Final cleaned dataset
│
├── tests/                       # Unit tests to ensure code correctness
│   ├── test_data_preparation.py
│   └── test_data_analysis.py
│
├── requirements.txt            # Required Python libraries for the project
├── .gitignore                  # Files and directories to be excluded from version control
└── README.md                   # Project documentation
```

### How to Use This Repository

1. **Clone the repository**:

   Run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/madratak/DIQ_Project2024.git

2. **Set up the environment**:

   Install dependencies via pip:
   
   ```bash
   pip install -r requirements.txt

3. **Data Loading and Cleaning**:

   The raw dataset is stored in ```data/raw/Comune-di-Milano-Servizi-alla-persona-parrucchieri-estetisti.csv```.
   Data cleaning and transformation scripts are in the ```src/data_preparation.py``` file.
   Once cleaned, the dataset is saved in ```data/cleaned/```.

4. **Analysis**:

   After cleaning, data analysis (e.g., clustering, regression) can be run using the Jupyter notebooks located in the ```notebooks/``` directory.

### Collaborators

This project is a collaborative effort between:

- [Mauro Orazio Drago](https://github.com/madratak)
- [Dennis Pierantozzi](https://github.com/DennisPierantozzi)
- [Davide Morelli](https://github.com/DavideMorelli)
