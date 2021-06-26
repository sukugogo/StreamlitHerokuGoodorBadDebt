import streamlit as st
import pandas as pd
import math


def fn_calc_results(input_list):
    total_cash = input_list[0]
    home_cost = input_list[1]
    user_down_amt = input_list[2]
    loan_period = input_list[3]
    loan_rate = input_list[4]
    invest_rate = input_list[5]

    principal_amt = total_cash - user_down_amt
    round_to = 0
    loan_fractional_rate = loan_rate/1200
    loan_emi = round(
        (loan_fractional_rate * principal_amt)
        / (1 - pow((1 + loan_fractional_rate), -1 * loan_period * 12))
        , 2)
    tot_loan_accrued_amt = round(loan_emi * loan_period * 12, round_to)
    tot_loan_interest_amt = round(tot_loan_accrued_amt - principal_amt, round_to)

    loan_table_data = {'ColName': ['Loan Amount', 'Loan Rate', 'Total Accrued Amount', 'Interest Amount'],
                       'ColValue': [principal_amt, loan_rate, tot_loan_accrued_amt, tot_loan_interest_amt]}

    tot_invest_interest_amt = round(principal_amt * (pow(1 + (invest_rate/100), loan_period) - 1), round_to)
    tot_invest_accrued_amt = round(tot_invest_interest_amt + principal_amt, round_to)

    invest_table_data = {'ColName': ['Invested Amount', 'Return Rate', 'Total Accrued Amount', 'Interest Amount'],
                         'ColValue': [principal_amt, invest_rate, tot_invest_accrued_amt, tot_invest_interest_amt]}
    return loan_table_data, invest_table_data, [tot_loan_interest_amt, tot_invest_interest_amt]


def fn_column_compare(input_list):
    loan_table_data, invest_table_data, interest_amt_list = fn_calc_results(input_list)
    df_loan = pd.DataFrame.from_dict(loan_table_data)
    df_invest = pd.DataFrame.from_dict(invest_table_data)

    col1, col2 = st.beta_columns(2)
    col1.header('Loan')
    col1.dataframe(df_loan)

    col2.header('Investment')
    col2.dataframe(df_invest)


    return interest_amt_list

