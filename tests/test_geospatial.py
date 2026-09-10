from geospatial.agent import run_geospatial_demo
def test_geo():
    out = run_geospatial_demo()
    assert out['status']=='demo'
