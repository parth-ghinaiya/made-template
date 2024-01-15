# Analysis Report: Correlations of Gold Price and Crude Oil Price Among Major Economies (1983-2020)

## Overview
This project focuses on analyzing the correlations between gold prices and crude oil prices across major economies from 1983 to 2020. The dataset for this analysis is sourced from Kaggle, and authentication is required to access the dataset.

## Technologies Used
- **Python**: Data analysis and visualization are performed using Python programming language.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib and Seaborn**: Used for creating visualizations to better understand the trends.
- **Kaggle API**: Utilized for accessing the dataset.

## Kaggle Authentication
To access the dataset from Kaggle, follow these steps:

1. Go to [Kaggle Account Settings](https://www.kaggle.com/settings).
2. Download your Kaggle API key as a `kaggle.json` file.
3. Place the `kaggle.json` file inside the `/project/` directory.

**Filepath:** `/project/kaggle.json`

```json
{
  "username": "par****a",
  "key": "dc5c*******************01"
}
```

## Set Execute Permissions for the Pipeline Script
Before running the analysis pipeline, ensure that the pipeline script has execute permissions. Run the following command:

```bash
chmod +x ./project/pipeline.sh
```

## Run the Analysis Pipeline
Navigate to the project directory and execute the pipeline script:

```bash
cd project && ./pipeline.sh
```

## Set Execute Permissions for the Test Pipeline Script
If you want to run the test pipeline, grant execute permissions to the test script:

```bash
chmod +x ./project/tests.sh
```

## Run the Test Pipeline
Navigate to the project directory and execute the test script:

```bash
cd project && ./tests.sh
```

## Analysis Report
Explore the detailed analysis report [here](https://github.com/parth-ghinaiya/made-template/blob/main/project/report.ipynb).

This project aims to provide insights into the relationships between gold and crude oil prices, offering a comprehensive analysis of economic trends over the specified period. Feel free to explore and contribute to the analysis.