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
dld = quandl.get(x)
##############################
##timespread
df=dld
df=df.diff(axis=1)
##############################
