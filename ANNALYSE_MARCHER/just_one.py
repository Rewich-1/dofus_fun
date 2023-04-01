import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import time
import plotly.graph_objects as go
import plotly.express as px
import time
import datetime as dt
from datetime import date, timedelta ,datetime
import os
import gc
import sys

def read_valeur(valeur, start_date, end_date):
    df = pd.read_csv('../ROBOT_TREADER_V_3/valeur/' + valeur + '.csv')

    try:
        #df['date'] = pd.to_datetime(df['date'])
        df['date'] = datetime.strptime(str(df['date']), "%Y-%m-%d")

        #df['date'] = datetime.datetime.strptime(df['date'],'%Y-%m-%d')
        mask1 = (df['date'] >= datetime.strptime(str(start_date), "%Y-%m-%d")) & (df['date'] <= datetime.strptime(str(end_date), "%Y-%m-%d"))
        df = df.loc[mask1]
        df.set_index('date', inplace=True)
        return df
    except IOError:
        st.markdown('erreur')
        return

def app():
    print("ok")

    ticker_list = pd.read_csv('../ROBOT_TREADER_V_3/ressouces_V2.csv' , sep=';')

    st.markdown('''# Stock secteur''')
    st.write('---')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        start_date = st.date_input("Start date", dt.datetime.today().replace(day=1))
    with col2:
        end_date = st.date_input("End date", dt.datetime.today())
    with col3:
        colunne = st.selectbox('Stock secteur', ticker_list.columns)
    with col4:
        ressource =  st.selectbox('Stock secteur', ticker_list[colunne])

    df = pd.DataFrame()


    liste = [x for x in ticker_list[colunne] if str(x) not in ['nan', 'NaN', 'NAN']]
    j = 0

    # ======================================= CREATE DATEFRAME =======================================

    df = pd.read_csv('../ROBOT_TREADER_V_2/valeur/' + ressource + '.csv')
    df['date'] = pd.to_datetime(df['date'])

    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # ======================================= VIZU =======================================
    st.markdown('df')
    st.dataframe(df)

    fig = px.line(df, title='all valeur')
    st.plotly_chart(fig, use_container_width=True)

    st.bar_chart(df)


