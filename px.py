quandl.ApiConfig.api_key = "###"
NG = quandl.get("CHRIS/CME_NG1", collapse="daily")

no=range(1,10+1)
pit='CHRIS/CME_'
sym='NG'
colnum='.6'
x=[]
for i in no:
    z=pit.__add__(sym).__add__(str(i)).__add__(colnum)
    x.append(z)
##############################
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
##############################
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
##############################
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
