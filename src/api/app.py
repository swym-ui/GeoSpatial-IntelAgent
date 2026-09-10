from fastapi import FastAPI
from geospatial.agent import run_geospatial_demo
app = FastAPI(title='Geospatial Intelligence Demo API')
@app.get('/run')
def run():
    return {'status':'ok','result': run_geospatial_demo()}
