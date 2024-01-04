#!/bin/bash

# Export kaggle.json to os env for Kaggle authentication
KAGGLE_JSON_PATH="./kaggle.json"
KAGGLE_CONFIG_DIR=$(dirname "$KAGGLE_JSON_PATH")
export KAGGLE_CONFIG_DIR

# Install required packages from requirements.txt
pip install --upgrade pip
pip install -r ./requirements.txt

# Run your Python file
pytest ./test_pipeline.py

echo "pytest script has been completed"