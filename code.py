import streamlit as st

st.title("Even or Odd Number Checker")

num = st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if num % 2 == 0:
        st.success("The number is Even.")
    else:
        st.warning("The number is Odd.")
