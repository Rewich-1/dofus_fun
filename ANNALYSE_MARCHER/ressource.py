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

import psycopg2
import unicodedata
import unidecode
import pandas.io.sql as psql

def read_valeur(valeur, start_date, end_date):

    conn = psycopg2.connect(
        host="86.252.168.180",
        database="postgres",
        user="postgres",
        password="postgres")

    cur = conn.cursor()



    resource_bdd = valeur.lower()
    resource_bdd = unidecode.unidecode(resource_bdd, 'utf-8')
    resource_bdd = str(resource_bdd)
    resource_bdd = resource_bdd.replace(" ", "_").replace("-", "_").replace("'", "_").replace("`", "_").replace(":", "_")


    sql = 'select date(date) ,floor(avg(prix_100)) from ortie where date BETWEEN '+start_date+' and '+end_date +'group by date(date)'
    cur.execute('select date(date) ,floor(avg(prix_100)) from '+resource_bdd+' where date BETWEEN '+start_date+' and '+end_date+' group by date(date)')

    #cnxn = pyodbc.connect(conn)
    #df = psql.frame_query(sql, cnxn)
    #version = cur.fetchall()
    df = pd.DataFrame(cur.fetchall())
    df.columns = ['date', valeur]
    df.set_index('date', inplace=True)




   # df = pd.read_csv('../ROBOT_TREADER_V_3/valeur/' + valeur + '.csv')


    #try:
        #df['date'] = pd.to_datetime(df['date'])
        #df['date'] = pd.to_datetime(df['date'])
        #df['date'] = datetime.datetime.strptime(df['date'],'%Y-%m-%d')
        #mask1 = (df['date'] >= datetime.strptime(str(start_date), "%Y-%m-%d")) & (df['date'] <= datetime.strptime(str(end_date), "%Y-%m-%d"))
        #df = df.loc[mask1]
        #df.set_index('date', inplace=True)
    return df
    #except IOError:
    #    st.markdown('erreur')
    #    return

def app():

    print("ok")

    ticker_list = pd.read_csv('../ROBOT_TREADER_V_3/ressouces_V2.csv' , sep=';')

    st.markdown('''# Stock secteur''')
    st.write('---')
    col1, col2, col3 = st.columns(3)

    with col1:
        start_date = st.date_input("Start date", dt.datetime.today().replace(day=1))
    with col2:
        end_date = st.date_input("End date", dt.datetime.today())
    with col3:
        colunne = st.selectbox('Stock secteur', ticker_list.columns)

    df = pd.DataFrame()



    start_date= str(start_date)
    start_date = "'"+start_date+"'"

    end_date = str(end_date)
    end_date = "'" + end_date + "'"





    liste = [x for x in ticker_list[colunne] if str(x) not in ['nan', 'NaN', 'NAN']]
    j = 0

    # ======================================= CREATE DATEFRAME =======================================
    for idx, i in enumerate(ticker_list[colunne]):


        #st.dataframe(df)

        if idx < len(liste):
            #df = pd.read_csv('../ROBOT_TREADER_V_2/valeur/' + i + '.csv')
            try:
                if j == 0:

                    tickerDf1 = read_valeur(i, start_date, end_date)
                    # st.dataframe(tickerDf1.iloc[:, 0])
                    tickerDf1.rename(columns={'prix100': i},inplace=True)
                    df = tickerDf1.iloc[:, 0]

                    del tickerDf1
                else:
                    tickerDf1 = read_valeur(i, start_date, end_date)
                    tickerDf1.rename(columns={'prix100': i},inplace=True)

                    df = pd.merge(df, tickerDf1.iloc[:, 0], how='outer', left_index=True,right_index=True)


                    gc.collect()
            except:
                st.markdown('fail for ' + str(i))
            j += 1

    valour = pd.DataFrame(columns=['tickerData', 'start', 'end', 'move'])

    st.dataframe(df)
    for i in list(df.columns):
        j = 0
        # st.markdown(df[i].iloc[j].notnull().values.any())

        while str(df[i].iloc[j]) in ['nan', 'NaN', 'NAN', 'NULL'] and str(df[i].iloc[j]) != str(df[i].iloc[-1]):
            j = j + 1

        liste2 = [x for x in df[i] if str(x) not in ['nan', 'NaN', 'NAN']]

        #st.markdown(j)
        #st.markdown(liste2[0])
        #st.markdown(liste2[-1])
        #st.markdown('________________________________________________________')

        if (liste2[0] != 0 and liste2[-1] != 0):

            valour = valour.append({'tickerData': i, 'start': liste2[0], 'end': liste2[-1],
                                    'move': int(((liste2[-1] * 100) / liste2[0]) - 100)}, ignore_index=True)
        j = 0


    fig = px.line(df, title='all percent')
    st.plotly_chart(fig, use_container_width=True)


 # ======================================= METRIC =======================================
    valour = valour.fillna(0)
    st.dataframe(valour)
    st.title("best")
    st.write('---')
    cols = st.columns(3)
    for i in range(1, 4):
        with cols[i - 1]:

            st.metric(valour.sort_values(by='move').iloc[-i]['tickerData'],
                      int(valour.sort_values(by='move').iloc[-i]['end']),
                      int(valour.sort_values(by='move').iloc[-i]['move']))

    st.title("looser")
    st.write('---')
    cols = st.columns(3)
    for i in range(1, 4):
        with cols[i - 1]:
            st.metric(valour.sort_values(by='move').iloc[i - 1]['tickerData'],
                      int(valour.sort_values(by='move').iloc[i - 1]['end']),
                      int(valour.sort_values(by='move').iloc[i - 1]['move']))


