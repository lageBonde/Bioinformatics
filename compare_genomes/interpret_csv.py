import csv
import matplotlib.pyplot as plt
from scipy.signal.windows import gaussian
import numpy as np


with open('bysearch_tata.csv', newline='\n') as csvfile:
    datapoints = [float(i[1]) for i in csv.reader(csvfile, delimiter=',', quotechar='|')]
    
    #datapoints = [i for i in datapoints if i > -50]
    datapoints = sorted(datapoints,key=float)

    plt.plot(
        range(len(datapoints)),
        datapoints
    )
    plt.savefig("bysearch_tata")