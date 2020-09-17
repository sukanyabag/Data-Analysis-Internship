import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import streamlit as st
sns.set(font_scale=1.4)

st.title('Covid-19 Data Analysis')
covid19_df = pd.read_csv("covid_19_india.csv")
individuals_df = pd.read_csv("IndividualDetails.csv")

data= pd.read_csv('IndividualDetails.csv')
plt.figure(figsize=(16,20))
with sns.axes_style('white'):
    g = sns.factorplot(y ="detected_state", data=data, aspect=1.5,
                       kind="count", color='red', height=8, hue='gender')
    g.set_xticklabels(step=1)


st.pyplot()

df = pd.DataFrame([14,44,129,94,66,74,58,9,4,1], index=['0-10', '11-20', '21-30', '31-40', '41-50'
, '51-60', '61-70', '71-80', '81-90', '91-100'], columns=['x'])

# make the plot
df.plot(kind='pie', subplots=True, figsize=(8, 8))

st.pyplot()

Male = (data['current_status'] == 'Deceased') & (data['gender'] == 'Female')



df = pd.DataFrame([18,31,975], index=['Deceased', 'Recovered', 'Hospitalized'], columns=['x'])

# make the plot
df.plot(kind='pie', subplots=True, figsize=(8, 8))
st.pyplot()

covid19_df_latest = covid19_df[covid19_df['Date']=="18/08/20"]

covid19_df_latest = covid19_df_latest.sort_values(by=['Confirmed'],ascending = False)
plt.figure(figsize=(12,8),dpi = 80)
plt.bar(covid19_df_latest['State/UnionTerritory'][:5],covid19_df_latest['Confirmed'][:5],align='center',color='lightgrey')
plt.ylabel('Number of confirmed cases')
plt.title('States with maximum confirmed cases')

st.pyplot()


covid19_df_latest = covid19_df_latest.sort_values(by=['Deaths'],ascending = False)
plt.figure(figsize=(12,8), dpi=80)
plt.bar(covid19_df_latest['State/UnionTerritory'][:5], covid19_df_latest['Deaths'][:5], align='center',color='lightgrey')
plt.ylabel('Number of Deaths')
plt.title('States with maximum deaths')

st.pyplot()

covid19_df_latest['Deaths/Confirmed Cases'] = (covid19_df_latest['Confirmed']/covid19_df_latest['Deaths']).round(2)
covid19_df_latest['Deaths/Confirmed Cases'] = [np.nan if x==float("inf") else x for x in covid19_df_latest['Deaths/Confirmed Cases']]
covid19_df_latest = covid19_df_latest.sort_values(by=['Deaths/Confirmed Cases'], ascending=True,na_position='last')
plt.figure(figsize=(10,8),dpi=80)
sns.heatmap(covid19_df_latest.corr(),annot=True)
st.pyplot()

individuals_grouped_district = individuals_df.groupby('detected_district')
individuals_grouped_district = individuals_grouped_district['id']
individuals_grouped_district.columns=['count']

individuals_grouped_gender = individuals_df.groupby('gender')
individuals_grouped_gender = pd.DataFrame(individuals_grouped_gender.size().reset_index(name='count'))
individuals_grouped_gender.head()

plt.figure(figsize=(10,6),dpi=80)
barlist= plt.bar(individuals_grouped_gender['gender'],individuals_grouped_gender['count'],align='center',color='grey',alpha=0.3)
barlist[1].set_color('r')
plt.ylabel('Count',size=12)
plt.title('Count on the basis of gender',size=16)

st.pyplot()
