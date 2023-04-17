import numpy as np
import waveresponse as wr
import cmath
import matplotlib.pyplot as plt


def CalculateWaveResponse(data):
    freq = np.linspace(0.2, 1.3, 23)
    #freq =  np.linspace(1, 10, 4287, endpoint=False)
    print(freq)
    dirs = np.linspace(0., 1, 1)
    print("f-len:{0}".format(len(freq)))
    print("dirs-len:{0}".format(len(dirs)))
    spectrum = wr.JONSWAP(freq, freq_hz=True)

    #vals = np.array(np.abs(data[0]))
    vals = []
    for mag in np.abs(data[0]):
        vals.append([mag])
    
    print(vals)
    print(len(vals))
    #for pnl in data:
    #    vals.append(np.abs(data[pnl]))

    rao = wr.RAO(freq, dirs, vals)
    #wp = wr.WaveSpectrum(freq,dirs,vals)
    
    hs = 5.2
    tp = 11.9

    new_freq, one_d_new_vals = spectrum(hs, tp, gamma=2.351)
    print("new_freq:{0}\nnew_vals:{1}".format(new_freq, one_d_new_vals))
    

    #make 2 D new values
    two_d_new_vals = []
    for val in one_d_new_vals:
        two_d_new_vals.append([val])

    #rao.interpolate(new_freq, dirs, )
    wp = wr.WaveSpectrum(new_freq,dirs,two_d_new_vals)
    res = wr.calculate_response(rao,wp,0)
    
    new_calculated_vals= res.grid()[2]
    
    plt.plot(new_calculated_vals)
    plt.plot(vals)
    plt.show()
    #print(new_calculated_vals)
    
    
    #plt.plot(vals)
    #plt.ylabel('some numbers')
    #plt.show()


data = {}

handle = open ('PressureForEachHeading.csv', 'r')
count = 0
for line in handle.readlines():
    parts = line.split(';')
    p = int(parts[0])
    f = parts[1]
    h = parts[2]
    real = parts[3]
    img = parts[4]
    
    count +=1
    #print(count)
    if p in data:
        data[p].append(complex(float(real),float(img)))
    else:
        data[p] = [complex(float(real),float(img))]
        #print(p) 


CalculateWaveResponse(data)
