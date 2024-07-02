from fastapi import FastAPI
import xgboost as xgb
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from classes import ExperienceLevelItem, JobTitleItem, LocationItem

app = FastAPI()

xgb_model = xgb.XGBRegressor()
xgb_model.load_model("../xgb_salary_prediction_model.json")

label_encoder = LabelEncoder()


@app.get("/welcome")
def index(name):
    return {"Welcome": f"Hello, {name}"}


@app.post("/Data Engineer Salary Prediction")
def prediction(experience_level:ExperienceLevelItem, job_title:JobTitleItem, employee_residence:LocationItem,
               company_location:LocationItem):

    data = pd.DataFrame([{
        "experience_level": experience_level.value,
        "job_title": job_title.value,
        "employee_residence": employee_residence.value,
        "company_location": company_location.value
    }])

    data["job_title"] = data["job_title"].map({"Data Scientist": 0, "Data Analyst": 1, "Data Engineer": 2, "Machine Learning Engineer": 3, "Research Scientist": 4})
    data["experience_level"] = data["experience_level"].map({"SE": 0, "MI": 1, "EN": 2, "EX": 3})
    data["company_location"] = data["company_location"].map({"US": 0, "GB": 1, "CA": 2, "ES": 3})
    data["employee_residence"] = data["employee_residence"].map({"US": 0, "GB": 1, "CA": 2, "ES": 3})

    pred = xgb_model.predict(data)

    return {"Expected Salary": f"{pred[0]} USD"}