import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/survey_results")
df = pd.read_csv("survey_results_public.csv")
df.to_sql("survey_results_public", engine)
