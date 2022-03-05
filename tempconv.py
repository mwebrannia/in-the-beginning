import streamlit as st

st.header('''Temperature Conversion App''')
st.write('''*slide the slider to convert value to Celcius*''')
value = st.slider('val')

st.write(value, '°F is ', (value * 9/5) + 32, '°C')