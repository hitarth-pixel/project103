import pandas as pd
import plotly_express as px
df=pd.read_csv("proData.csv")
fig=px.scatter(df,x="date",y="cases",color="country",size_max=100)
fig.show()