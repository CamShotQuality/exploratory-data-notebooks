# Exploratory Data Notebooks

This repository contains Jupyter notebooks and related resources for exploratory data analysis and dataset cleansing. It serves as a workspace for:

- Data exploration and analysis
- Dataset cleaning and preprocessing
- Feature engineering
- Data quality assessment
- Statistical analysis and visualization

## Repository Structure

```
.
├── notebooks/               # Jupyter notebooks organized by purpose
│   ├── data_cleaning/      # Notebooks for data cleaning and preprocessing
│   ├── exploratory_analysis/ # Initial data exploration and analysis
│   ├── feature_engineering/ # Feature creation and transformation
│   ├── visualization/      # Data visualization notebooks
│   └── modeling/          # Statistical modeling and analysis
├── data/                   # Data storage
│   ├── raw/               # Original, immutable data
│   ├── processed/         # Cleaned, processed data ready for analysis
│   └── intermediate/      # Intermediate data files
└── docs/                  # Documentation and additional resources
```

## Environment Setup

This project uses `uv` for dependency management and virtual environment creation. To set up your environment:

1. Install `uv` if you haven't already:
   ```bash
   pip install uv
   ```

2. Run the setup script:
   ```bash
   ./setup_env.sh
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

4. Start Jupyter:
   ```bash
   jupyter notebook
   ```

The environment includes essential data science packages and Jupyter support. See `requirements.txt` for the complete list of dependencies.

## Purpose

The notebooks in this repository are designed to:
1. Explore and understand raw datasets
2. Clean and preprocess data for downstream analysis
3. Identify and handle missing values, outliers, and data inconsistencies
4. Create visualizations to better understand data patterns
5. Document the data transformation process

## Structure

Each notebook should follow a consistent structure:
1. Data loading and initial inspection
2. Data cleaning and preprocessing
3. Exploratory analysis
4. Documentation of findings and transformations

## Best Practices

When working with these notebooks:
- Document all data transformations and their rationale
- Include clear markdown cells explaining the analysis process
- Save intermediate cleaned datasets when appropriate
- Use consistent naming conventions for variables and functions
- Include data validation checks where necessary

## Getting Started

1. Clone this repository
2. Install required dependencies (if any)
3. Open the relevant notebook for your analysis
4. Follow the documented process for data exploration and cleaning
