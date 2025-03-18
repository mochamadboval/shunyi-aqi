import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

aqi_df = pd.read_csv(os.path.join(os.path.dirname(__file__), "main_data.csv"))
year = 2016

with st.sidebar:
  st.header("Shunyi AQI by Mochamad Boval")
  
  year = st.selectbox(
    label="Lihat berdasarkan tahun:",
    options=(2013, 2014, 2015, 2016, 2017),
    index=3
  )

aqi_by_year = aqi_df[aqi_df["year"] == year]


st.subheader(f"Rata-rata PM2.5 dan PM10 per bulan ({year})")
col_1, col_2 = st.columns(2)

with col_1:
  PM2_by_month = round(aqi_by_year.groupby("month")["PM2.5"].mean(), 1).reset_index()

  fig, ax = plt.subplots(figsize=(10, 5))
  ax.plot(
      pd.to_datetime(PM2_by_month["month"], format="%m").dt.strftime("%b"),
      PM2_by_month["PM2.5"],
      marker="o", 
      linewidth=2,
      color="#ef4444"
  )
  ax.set_title("PM2.5", loc="center", fontsize=18)
  ax.tick_params(axis="y", labelsize=12)
  ax.tick_params(axis="x", labelsize=12)
  
  st.pyplot(fig)

with col_2:
  PM10_by_month = round(aqi_by_year.groupby("month").PM10.mean(), 1).reset_index()

  fig, ax = plt.subplots(figsize=(10, 5))
  ax.plot(
      pd.to_datetime(PM10_by_month["month"], format="%m").dt.strftime("%b"),
      PM10_by_month["PM10"],
      marker="o", 
      linewidth=2,
      color="#eab308"
  )
  ax.set_title("PM10", loc="center", fontsize=18)
  ax.tick_params(axis="y", labelsize=12)
  ax.tick_params(axis="x", labelsize=12)
  
  st.pyplot(fig)

st.subheader(f"Rata-rata PM2.5 dan PM10 per tanggal ({year})")

PM2_by_day = round(aqi_by_year.groupby("day")["PM2.5"].mean(), 1).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
ax = sns.barplot(
  y="PM2.5",
  x="day",
  data=PM2_by_day,
  color="#fca5a5"
)

for count in ax.containers:
  ax.bar_label(count, fontsize=8)

ax.set_title("PM2.5", loc="center", fontsize=18)
ax.set_ylabel(None)
ax.tick_params(axis="x", labelsize=12)

st.pyplot(fig)

PM10_by_day = round(aqi_by_year.groupby("day").PM10.mean(), 1).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
ax = sns.barplot(
  y="PM10",
  x="day",
  data=PM10_by_day,
  color="#fde047"
)

for count in ax.containers:
  ax.bar_label(count, fontsize=8)

ax.set_title("PM10", loc="center", fontsize=18)
ax.set_ylabel(None)
ax.tick_params(axis="x", labelsize=12)

st.pyplot(fig)