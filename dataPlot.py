import os,sys
import numpy as np
import matplotlib.pyplot as plt

# script for plotting data from OpenFOAM cases

fp = './data/Ux_yLine.csv'

# ================================================

def fetchData(filename):
    f = open(filename,'r')
    # skipping header
    f.readline()
    l = []
    try:
        while f.readline():
            for line in f:
                line = line.split()[0].split(sep=',')
                l.append(line)
        arr = np.array(l).astype(float)
    except:
        print('Cannot reach data correctly')

    f.close()
    return arr

def plotData(data,xlabel='',ylabel='',grid=False,title='',linecolor='black',marker='o',linestyle='-'):
    """ Plots x,y data passed as a list. """

    # Preparing plot area
    if grid : plt.grid(color='grey',linestyle='--',linewidth=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    #plt.xticks([])
    #plt.yticks([])
    ax = plt.subplot(111)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    x,y = data[0],data[1]
    
    ax.plot(x,y,color=linecolor,marker=marker,linestyle=linestyle,
            markersize=1.5, markeredgecolor=linecolor,fillstyle='none',
            markerfacecolor=linecolor)
    #plt.plot(x,y)

    plt.show()

# ================================================
if __name__ == '__main__':

    data = fetchData(fp)
    x,ux = data[:,-2],data[:,0]

    data = [x,ux]
    plotData(data,xlabel="h/y [m]",ylabel="Ux [m/s]",grid=True)
