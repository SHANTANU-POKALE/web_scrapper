import streamlit as st
import plotly.express as px
import sqlite3


connection = sqlite3.connect("temp.db")
cursor = connection.cursor()
cursor.execute("SELECT date FROM temperatures")
date = cursor.fetchall()
dateemp = [item[0] for item in data]

cursor.execute("SELECT temperature FROM temperatures")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figure = px.line(x=df["date"], y=df["temperature"],
                 labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)