import pandas as pd
import streamlit as st
import hydralit_components as hc

df_log = pd.read_csv("login_logs.csv")
df_s_or = pd.read_csv("sales_orders.csv")
df_o_it = pd.read_csv("sales_orders_items.csv")
st.sidebar.subheader('Plantix - Retailer App Case Study')
df_log['seconds']=pd.to_timedelta(df_log['login_time']).dt.total_seconds()

# total count of users
tot_users = len(df_log['user_id'].unique())
# how many users were there for amount of time.
def min_users(sec):
    data = df_log[df_log['seconds'] == sec]
    data = len(data['user_id'])
    return data
# finding number of times user logged-in in the app.
def user_log_time(ID):
    data = df_log[df_log['user_id'] == ID]
    data = len(data['login_time'])
    return data
# total stay time for an user
def user_sty_time(ID):
    data = df_log[df_log['user_id'] == ID]
    data = sum(data['seconds'])
    return data

# hc.info_card(title='Application User Count', content=tot_users, sentiment='good')
st.sidebar.metric(label='Total User Count', value=tot_users)
st.sidebar.metric(label='Minimum App Used Time (seconds)', value=min(df_log['seconds']))
st.sidebar.metric(label='User Count for Minimum Time', value=min_users(min(df_log['seconds'])))
st.sidebar.metric(label='Maximum App Used Time (minutes)', value= round((max(df_log['seconds']))/60,2))
st.sidebar.metric(label='User Count for Maximum Time', value=min_users(max(df_log['seconds'])))

cc = st.columns(3)
with cc[0]:
    st.header("Plantix - Case Study")
cc = st.columns(3)
with cc[0]:
    sel_user = st.selectbox("Select a User", df_log['user_id'].unique())
with cc[1]:
    st.metric(label='Count of User Logged-In (Lifetime)', value=user_log_time(sel_user))
with cc[2]:
    st.metric(label='Total Stay time of User (in hours)', value=round(user_sty_time(sel_user)/3600,2))
   