# reading in from CSV and migrating data to sql database


import csv
import datetime

from app import models
from app.database import SessionLocal, engines

db = SessionLocal()
models.Base.metadata.create_all(bind=engine)

with open("sars_2003_complete_dataset_clean.csv", "r") as f:
    for row in csv_reader:
        db_record = models.Record(
            date = datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
            country = row["country"],
            cases=row["cases"],
            deaths=row["deaths"],
            recoveries=row["recoveries"],                                  
        )