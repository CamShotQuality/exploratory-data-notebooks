#!/bin/bash

# Create virtual environment using uv
uv venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies using uv
uv pip install -r requirements.txt

# Install ipykernel for Jupyter
python -m ipykernel install --user --name=exploratory-data --display-name="Exploratory Data Analysis"

echo "Virtual environment setup complete!"
echo "To activate the environment, run: source .venv/bin/activate" 