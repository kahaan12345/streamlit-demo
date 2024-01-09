import streamlit as st

st.title("Hello This Is My First App.")

i1 = st.text_input("Enter an integer")
i2 = st.text_input("Enter another integer")

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

date = st.date_input("Selct your desired date")

submit = st.button("Calculate sum")

if submit:
    st.write(f"The Sum of the given integer is { int(i1)+int(i2) }")
    st.write(f"Your selected option is {option}")
    st.write(f"Your selected date is {date}")