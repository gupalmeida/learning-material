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

def plotData(data,xlabel='',ylabel='',grid=False,title='',linecolor='black',marker='o',linestyle='-',
        save_img=False,img_name='image.png'):
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

    if save_img : plt.savefig(img_name,dpi=300)

def plotWave(data,xlabel='',ylabel='',grid=False,title='',linecolor='black',
        marker='o',linestyle='-', leveled=False,amp=1,level=0,hide_labels=False,
        save_img=False,img_name='image.png',display=False):
    """ Plots sinosoidal wave from data passed as a list. """

    # Preparing plot area
    if grid : plt.grid(color='grey',linestyle='--',linewidth=0.5)
    plt.xlabel(xlabel,labelpad=100,fontsize=16)
    plt.ylabel(ylabel,labelpad=30,fontsize=16)
    plt.title(title)
    #plt.xticks([])
    #plt.yticks([])
    ax = plt.subplot(111)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    if hide_labels:
        ax.set_xticklabels([])
        ax.set_yticklabels([])

    x,y = data[0],data[1]
    
    ax.plot(x,y,color=linecolor,linestyle=linestyle,linewidth=1.3)
    #plt.plot(x,y)

    if leveled:
        bx = plt.subplot(111)
        bx.spines['right'].set_visible(False)
        bx.spines['top'].set_visible(False)
        bx.spines['bottom'].set_position(('data',0))
        bx.spines['left'].set_position(('data',0))
        if hide_labels:
            bx.set_xticklabels([])
            bx.set_yticklabels([])

        y1 = amp * np.sin(x) + level
        bx.plot(x,y1,color='red',linestyle='--',linewidth=1.3)

    plt.legend(['Sinusoidal Wave','Leveled Sinusoidal Wave'])
    plt.figure(num=1,figsize=(15,20),dpi=300)

    if save_img : plt.savefig(img_name,dpi=300)

    if display : plt.show()

# ================================================
if __name__ == '__main__':

    data = fetchData(fp)
    x,ux = data[:,-2],data[:,0]

    #data = [x,ux]
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)
    data = [x,y]

    plotWave(data,xlabel="Time",ylabel="U(t)",grid=True,
            linecolor='blue',leveled=True,amp=1.0,level=1.0,hide_labels=True,
            save_img=True,img_name='sinusoidalWave.png',display=False)
