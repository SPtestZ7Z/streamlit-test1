import streamlit as st
import pandas as pd
import numpy as np

st.title("hello world")

st.header("This is a header with a divider", divider='rainbow')

st.markdown("Welcome to our app where you can get free advice")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
