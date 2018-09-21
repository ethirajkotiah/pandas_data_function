import numpy as np
import pandas as pd
from pandas.plotting import autocorrelation_plot, lag_plot
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def df_derived_by_shift(df,lag=0,NON_DER=[]):
    df = df.copy()
    if not lag:
        return df
    cols ={}
    for i in range(1,lag+1):
        for x in list(df.columns):
            if x not in NON_DER:
                if not x in cols:
                    cols[x] = ['{}_{}'.format(x, i)]
                else:
                    cols[x].append('{}_{}'.format(x, i))
    for k,v in cols.items():
        columns = v
        dfn = pd.DataFrame(data=None, columns=columns, index=df.index)    
        i = 1
        for c in columns:
            dfn[c] = df[k].shift(periods=i)
            i+=1
        df = pd.concat([df, dfn], axis=1, join_axes=[df.index])
    return df

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
    
