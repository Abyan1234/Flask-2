import pandas as pd
import numpy as np

df=pd.read_csv('articles.csv')

C=df['eventType'].mean()
m=df['contentType'].quantile(0.9)

q_articles=df.copy().loc[df['contentType']>=m]

def weighted_rating(x,m=m,C=C):
    v=x['contentType']
    R=x['eventType']
    return(v/(v+m)*R)+(m/(m+v)*C)

q_articles['score']=q_articles.apply(weighted_rating,axis=1)
q_articles=q_articles.sort_values('score',ascending=False)
output=q_articles[['index','timestamp','title','eventType','contentId','authorSessionId']].head(20).values.tolist()


