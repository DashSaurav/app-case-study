import streamlit as st
import datetime
import calendar
from home import home_ana
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Retail App Analytics', layout='wide')

st.header("Case Study - Retail App Analytics")
currenttime = datetime.datetime.today()
onlydate = currenttime.day
onlymonth = currenttime.strftime("%b")
onlyyear = currenttime.year
onlyday = calendar.day_name[currenttime.weekday()]
st.sidebar.info(f"""{onlyday} , {onlydate} {onlymonth} {onlyyear}""")

with st.sidebar:
    sel = option_menu(
        menu_title="Main Menu",
        options=["Home"],
        icons=["tv"],
        menu_icon="cast",
        #default_index=0,
    )

# sel = st.sidebar.radio("Select a Page",('Analysis', 'Predection'))

if sel=='Home':
    home_ana()
