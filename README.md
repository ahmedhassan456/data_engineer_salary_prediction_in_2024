# Data Engineer Salary Prediction 2024 using LGBM and FastAPI Deployment

## Project Overview

This project aims to predict the salaries of data engineers for the year 2024 using a machine learning model based on LightGBM (LGBM). The model is deployed using FastAPI to serve predictions via a web API.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [API Deployment](#api-deployment)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this project is to provide an accurate prediction of data engineer salaries based on various features such as experience level, employment type, job title, company location, and more. This can help employers, job seekers, and analysts understand the salary trends and make informed decisions.

## Dataset

The dataset provides insights into data engineer salaries and employment attributes for the year 2024. It includes the following features:

- **work_year**: The year in which the data was collected (2024).
- **experience_level**: The experience level of the employee, categorized as SE (Senior Engineer), MI (Mid-Level Engineer), or EL (Entry-Level Engineer).
- **employment_type**: The type of employment, such as full-time (FT), part-time (PT), contract (C), or freelance (F).
- **job_title**: The title or role of the employee within the company, for example, AI Engineer.
- **salary**: The salary of the employee in the local currency (e.g., 202,730 USD).
- **salary_currency**: The currency in which the salary is denominated (e.g., USD).
- **salary_in_usd**: The salary converted to US dollars for standardization purposes.
- **employee_residence**: The country of residence of the employee.
- **remote_ratio**: The ratio indicating the extent of remote work allowed in the position (0 for no remote work, 1 for fully remote).
- **company_location**: The location of the company where the employee is employed.
- **company_size**: The size of the company, often categorized by the number of employees (S for small, M for medium, L for large).

## Features

- **Prediction Model**: The model uses LightGBM (LGBM) for regression to predict salaries.
- **API Deployment**: The FastAPI framework is used to deploy the model as a web API for serving predictions.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/data-engineer-salary-prediction.git
    cd data-engineer-salary-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Model Training**: Run the Jupyter notebook to train the model.
2. **API Deployment**: Use FastAPI to deploy the model.

## Model Training

The notebook includes the following steps:

1. **Data Preprocessing**: Load and preprocess the dataset.
2. **Feature Engineering**: Create features relevant for model training.
3. **Model Training**: Train the LightGBM model.
4. **Model Evaluation**: Evaluate the model's performance using metrics like mean squared error.

## API Deployment

To deploy the API using FastAPI:

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
