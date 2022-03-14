import pytest
import app
import os 

# content of test_sample.py
#def inc(x):
    #return x + 1

#def test_answer():
    #assert inc(4) == 5

#loop through all plugins to make sure they import
def test_plugins():
    import plugins.weather as weather
    import plugins.speed_test as speed_test
    import plugins.air_quality as air_quality
    assert 0==0

def test_rick_exists():
    #isFile = 1
    isFile = os.path.isfile("rickrollshort.wave") 
    assert isFile == 1