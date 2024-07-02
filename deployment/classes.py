from enum import Enum
from pydantic import BaseModel

class ExperienceLevelItem(str, Enum):
    SE = "SE"
    MI = "MI"
    EN = "EN"
    EX = "EX"

class JobTitleItem(str, Enum):
    data_engineer = "Data Engineer"
    data_scientist = "Data Scientist"
    data_analyst = "Data Analyst"
    machine_learning_engineer = "Machine Learning Engineer"
    research_scientist = "Research Scientist"

class LocationItem(str, Enum):
    US = "US"
    GB = "GB"
    CA = "CA"
    ES = "ES"

class InputData(BaseModel):
    experience_level: ExperienceLevelItem
    job_title: JobTitleItem
    employee_residence: LocationItem
    company_location: LocationItem