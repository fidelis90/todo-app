import streamlit as st

st.title("Book Holyswagger")

event_month = st.selectbox("Select the month of the event:", [
                           "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
event_day = st.number_input(
    "Enter the day of the event:", min_value=1, max_value=31)
event_year = st.number_input(
    "Enter the year of the event:", min_value=2023, max_value=2030)

event_date = f"{event_month} {event_day}, {event_year}"

if st.button("Book Artist"):
    st.success("Artist booked for event on: " + event_date)
