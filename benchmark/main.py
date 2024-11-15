from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    data = {"column1": [1, 2, 3], "column2": ["a", "b", "c"]}
    df = pd.DataFrame(data)
    return df.to_dict(orient="records")