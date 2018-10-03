import requests
import calendar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from pytz import UTC
import seaborn as sns
import datetime
import os
import api_wrapper as paw
reload(paw)
import plotly.plotly as py
import plotly.graph_objs as go
import np_utils
import GPy
# import pyflux
import stldecompose
import urllib2
import quandl
from ta import *
import scipy.signal
from scipy.signal import savgol_filter
def datecol(prism_p_history):
    pd.plotting.autocorrelation_plot(x)
    plt.show()
def datecol(prism_p_history):
    prism_p_history['Year'] = prism_p_history.index.year
    prism_p_history['Month'] = prism_p_history.index.month
    prism_p_history['week'] = prism_p_history.index.week
    prism_p_history['day'] = prism_p_history.index.day
    return prism_p_history
def crosscorr(datax, datay, lag=0):
    """ Lag-N cross correlation. 
    Parameters
    ----------
    lag : int, default 0
    datax, datay : pandas.Series objects of equal length

    Returns
    ----------
    crosscorr : float
    """
    return datax.corr(datay.shift(lag))
    
def autocorrplots(df_S,col_name,selectedLagPoints,maxLagDays):
    #%% show autocorr and lag plots
    temperatureDF=df_S
    col_name=cityToShow
    originalSignal = temperatureDF[cityToShow]
    # set grid spec of the subplots
    plt.figure(figsize=(12,6))
    gs = gridspec.GridSpec(2, len(selectedLagPoints))
    axTopRow = plt.subplot(gs[0, :])
    axBottomRow = []
    for i in range(len(selectedLagPoints)):
        axBottomRow.append(plt.subplot(gs[1, i]))

    # plot autocorr
    allTimeLags = np.arange(1,maxLagDays*24)
    autoCorr = [originalSignal.autocorr(lag=dt) for dt in allTimeLags]
    axTopRow.plot(allTimeLags,autoCorr); 
    axTopRow.set_title('autocorr Plot', fontsize=18);
    axTopRow.set_xlabel('time lag'); axTopRow.set_ylabel('correlation coefficient')
    selectedAutoCorr = [originalSignal.autocorr(lag=dt) for dt in selectedLagPoints]
    axTopRow.scatter(x=selectedLagPoints, y=selectedAutoCorr, s=50, c='r')

    # plot scatter plot of selected points
    for i in range(len(selectedLagPoints)):
        lag_plot(originalSignal, lag=selectedLagPoints[i], s=0.5, alpha=0.7, ax=axBottomRow[i])    
        if i >= 1:
            axBottomRow[i].set_yticks([],[])
    plt.tight_layout()
    plt.show()
    
####################################
quandl.ApiConfig.api_key = "Nu6VwzRQzz9pFXm2Ujwx"
NG = quandl.get("CHRIS/CME_NG1", collapse="daily")
df = add_all_ta_features(NG, "Open", "High", "Low", "Last", "Volume", fillna=True)
svgfilter = lambda x: savgol_filter(x,5,2)
df_smooth=df.apply(svgfilter)
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df.Settle)
plt.show()
##############################
