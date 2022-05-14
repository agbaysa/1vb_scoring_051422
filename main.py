import streamlit as st
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import time


model_dt = pickle.load(open('model_dt', 'rb'))

st.image('1vb.png')
st.header('First Valley Bank Loan Application Scoring')

with st.form('my_form'):
    st.write('Please encode the details of the Loan Application:')

    collateral = st.number_input('Enter Collateral Value (e.g. 1, 2, 3):', value= 1, key='collateral')
    assets = st.number_input('Enter Assets Value (e.g. 1, 2, 3):', value= 1, key='assets')
    ave_daily_sales = st.number_input('Enter Average Daily Sales Value (e.g. 1, 2, 3):', value= 1, key='ave_daily')
    adb_checking = st.number_input('Enter ADV Checking/Savings Value (e.g. 1, 2, 3):', value= 1, key='adb_checking')
    bap = st.number_input('Enter BAP Value (e.g. 1, 2, 3):', value= 1, key='bap')
    other_relevant = st.number_input('Enter Other Relevant Sources of Income Value (e.g. 1, 2, 3):', value= 1, key='other_relevant')
    coll_ownership = st.number_input('Enter Collateral Ownership Value (e.g. 1, 2, 3):', value= 1, key='coll_ownership')
    vb_adb = st.number_input('Enter First VAlley ADB (e.g. 1, 2, 3):', value= 1, key='vb_adb')
    score = st.number_input('Enter Score Value (e.g. 8, 10, etc.):', value= 1, key='score')
    age = st.number_input('Enter Age Value (e.g. 35, 56):', value= 25, key='age')
    prin = st.number_input('Enter Principal Value (e.g. 50000):', value= 30000, key='prin')
    amortamount = st.number_input('Enter Amortization Amount Value (e.g. 3500, 4630):', value= 5000, key='amortamount')
    loanterm = st.number_input('Enter Loan Term Value (e.g. 30, 60):', value= 30, key='loanterm')
    numberofamort = st.number_input('Enter Number of Amortization Value (e.g. 3, 6, 9, 12, 24, etc.):', value= 6, key='numberofamort')
    paymentinternal = st.number_input('Enter Payment Interval Value (e.g. 30, 90, etc.):', value= 30, key='ave_daily')

    submitted = st.form_submit_button('Get Application Rating')
    st.write('')

if submitted:

    progress = st.progress(0)
    my_status = 'Running calculations...'
    st.write(my_status)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    if collateral==None or assets==None or ave_daily_sales==None or adb_checking==None or bap==None or other_relevant==None or \
            coll_ownership==None or vb_adb==None or score==None or age==None or \
            prin == None or amortamount == None or loanterm==None or numberofamort==None or paymentinternal==None:
        st.warning('Please complete the details to compute the Loan Scoring or check the details if correct')
    else:

        df = pd.DataFrame(
            {'collateral': [collateral],
             'assets': [assets],
             'average daily sales': [ave_daily_sales],
             'adb checking savings': [adb_checking],
             'bap': [bap],
             'other relevant sources of income': [other_relevant],
             'collateral ownership': [coll_ownership],
             '1vb_adb': [vb_adb],
             'score': [score],
             'age': [age],
             'principal': [prin],
             'amortamount': [amortamount],
             'loanterm': [loanterm],
             'numberofamort': [numberofamort],
             'paymentinterval': [paymentinternal]
            }
        )

        st.write('')
        st.write('The following were the details provided:')
        st.dataframe(df)

        predict = model_dt.predict(df)

        st.write('')
        st.write('')
        st.write('Loan Application Decision:')
        st.write('')
        if predict == 0:
            st.success('The Loan Application is good. Please proceed with the booking of the loan.')
            st.balloons()
            st.warning('Please encode new details above if doing another loan scoring evaluation and click Get Application Rating button')

        else:
            st.warning('Please review the Loan Application further as.')
            st.warning('Please encode new details above if doing another loan scoring evaluation and click Get Application Rating button')
