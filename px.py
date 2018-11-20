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
import plotly.plotly as py
import plotly.graph_objs as go
import np_utils
import stldecompose
import urllib2
import quandl
from ta import *
import scipy.signal
from scipy.signal import savgol_filter

def quandlkey(a):
    return quandl.ApiConfig.api_key = a
#############################################################################################
##flat
def flatfutures(a,b,c):
#     no=range(1,10+1)
#     pit='CHRIS/CME_'
#     sym='NG'
#     colnum='.6'
    no=a
    pit=b
    sym=c
    colnum='.6'
    x=[]
    for i in no:
        z=pit.__add__(sym).__add__(str(i)).__add__(colnum)
        x.append(z)
    dld = quandl.get(x)
    return dld
#############################################################################################
##timespread
def timespread(a,b,c):
#     no=range(1,10+1)
#     pit='CHRIS/CME_'
#     sym='NG'
#     colnum='.6'
    no=a
    pit=b
    sym=c
    colnum='.6'
    x=[]
    for i in no:
        z=pit.__add__(sym).__add__(str(i)).__add__(colnum)
        x.append(z)
    dld = quandl.get(x)
    df=dld
    df=df.diff(axis=1)
    return df
#############################################################################################
def alltechindicators(NG):
    df = add_all_ta_features(NG, "Open", "High", "Low", "Last", "Volume", fillna=True)
    return df
#############################################################################################
def smoothsvgfilter(df,a,b):
    svgfilter = lambda x: savgol_filter(x,a,b)
    df_smooth=df.apply(svgfilter)
    return df_smooth
#############################################################################################
