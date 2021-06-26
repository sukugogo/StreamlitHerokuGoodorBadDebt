import streamlit as st
import functionscalc as fc


def fn_site_header():
    st.title('Good / Bad Debt Calculator')
    st.markdown("---")
    col1, col2 = st.beta_columns(2)

    col1.markdown('''
    So, you have built up a bit of a nest egg. Now you want to put all of it into your dream home. But what if you take 
    out a mortgage loan on the house and invest your hard earned money instead?
    
    This __Simple Calculator__ may help you decide! 
    
    Use the __Sidebar__ on the left to fill out your relevant details or review the default values as an insight on how 
    some debt could be actually good.  
    
    __Disclaimer:__ This calculator considers simple parameters and is a starting point for deciding whether one should
    get into debt. Actual decisions should factor in inflation, tax implications, tax breaks, investment risk etc before
    plunging into debt. 
     
    ''')
    col2.image('./Image/DebtYesNo.jpg', width=550)
    st.markdown("---")


def fn_site_results(interest_amt_list, input_list):
    total_cash = input_list[0]
    home_cost = input_list[1]
    loan_period = input_list[3]
    loan_rate = input_list[4]
    invest_rate = input_list[5]
    tot_loan_interest_amt = interest_amt_list[0]
    tot_invest_interest_amt = interest_amt_list[1]
    st.markdown("---")
    st.subheader("REVIEW YOUR RESULT BELOW")
    st.write(" ")
    col1, col2 = st.beta_columns(2)
    md_message1 = ""
    md_message2 = ""
    md_trailer2 = ""

    if tot_loan_interest_amt >= tot_invest_interest_amt or home_cost > total_cash:
        md_header = "__OH NO!!!__ Hold your horses on this one!"
        if home_cost > total_cash:
            md_message1 = "Cost of Home [" + str(home_cost) + \
                          "] is __Greater than__ your disposable Cash [" + str(total_cash) + "]."
        if tot_loan_interest_amt >= tot_invest_interest_amt:
            md_message1 = md_message1 + "Interest on Investment [" + str(tot_invest_interest_amt) + \
                          "] is __less than__ the interest on the loan [" + str(tot_loan_interest_amt) + "]."
        md_message2 = "Try not to go into Debt unless you have a net positive net-worth. If you are still adamant, \
        ensure that you have a significantly large nest egg and long term job security. Investing for rental income \
        is OK too provided the rental yield is high."
        md_trailer1 = "This Loan is a __BAD DEBT__."
        col2.image('./Image/ThumbsDown.jpg', width=260)
    else:
        md_header = "__Whoa!!!__ What sorcery is this? "
        md_message1 = "The investment return rate [" + str(invest_rate) + "%] is"
        if invest_rate > loan_rate:
            md_header = "__Great!!!__ We are now in the 'Obvious' Zone where this calculator is kind of useless."
            md_message1 = md_message1 + " __greater than__ the"
            md_trailer1 = " __Of Course__ this Loan would qualify as a Good Debt."
        elif invest_rate == loan_rate:
            md_message1 = md_message1 + " __equal to__ the"
            md_trailer1 = "__Yet,__"
        else:
            md_message1 = md_message1 + " __less than__ the"
            md_trailer1 = "__Yet,__"

        md_message1 = md_message1 + " the loan_rate [" + str(loan_rate) + "%]"
        md_trailer1 = md_trailer1 + " your earnings on your investment [" + str(tot_invest_interest_amt) \
                     + "] is still more that the interest you pay on the loan [" + str(tot_loan_interest_amt) + "]."
        md_trailer2 = "This Loan is a __GOOD DEBT__. Lucky you!!!"
        col2.image('./Image/ThumbsUp.jpg', width=330)

    col1.markdown(md_header)
    col1.markdown(md_message1)
    col1.markdown(md_message2)
    col1.markdown(md_trailer1)
    col1.markdown(md_trailer2)
    st.markdown("---")


def fn_sidebar_widget():
    st.subheader('  Provide Basic Input Below: ')
    total_cash = st.number_input('Enter Disposable Cash: ', value=120000)
    home_cost = st.number_input('Enter Cost of your Dream House: ', value=100000)
    user_down_amt = st.number_input('Enter Desired Down Payment: ', value=20000)
    loan_period = st.slider('Mortgage/Loan Tenure [years]: ', 1, 30, value=20)
    st.subheader('  Provide Interest Rates: ')
    loan_rate = st.slider('Mortgage/Loan Rate %: ', 0.1, 25.0, value=8.0)
    invest_rate = st.slider('Investment Return Rate %: ', 0.1, 25.0, value=3.6)

    return [total_cash, home_cost, user_down_amt, loan_period, loan_rate, invest_rate]


if __name__ == '__main__':
    app.listen(process.env.PORT)
    st.set_page_config(layout="wide", page_title="Good/Bad Debt Calculator")
    top_padding = 0
    padding = 5
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {top_padding}rem;
            padding-right: {padding}rem;
            padding-left: {padding}rem;
            padding-bottom: {padding}rem;
        }} </style> """, unsafe_allow_html=True)
    fn_site_header()

    with st.sidebar:
        input_list = fn_sidebar_widget()

    interest_amt_list = fc.fn_column_compare(input_list)
    fn_site_results(interest_amt_list, input_list)

