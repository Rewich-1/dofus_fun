import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import pydeck as pdk
import os
from datetime import datetime as dt
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import webbrowser

import ressource
import just_one
###################################################################################################

st.set_page_config(
    page_title="data finance DOFUS",
    page_icon="💸",
    layout='wide'
    )

st_folder = 'sp_app_solution'
os.makedirs(st_folder, exist_ok=True)



# MENU

PAGES = {
    "ressource": ressource,
    "just_one": just_one
}
st.sidebar.title('Menu')
selection = st.sidebar.radio("Select your page", list(PAGES.keys()))
page = PAGES[selection]
page.app()