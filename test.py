import numpy as np
import waveresponse as wr
import cmath
import matplotlib.pyplot as plt

def test():
    freq = np.linspace(0.0, 1.0, 50)
    print ("Fre length:{0}".format(len(freq)))
    dirs = np.linspace(0.0, 360.0, 10, endpoint=False)
    print ("Dir length:{0}".format(len(dirs)))
    vals = np.random.random((len(freq), len(dirs)))
    grid = wr.Grid(freq,dirs,vals,freq_hz=True,degrees=True,)
    #print(vals)


test()
exit()