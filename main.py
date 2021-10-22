import streamlit as st
import numpy as np
import pandas as pd

st.title('Sample streamlit app started with .exe')
st.write('Hello World!')

df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=list("ABCD"))
st.dataframe(df)

st.text('Done!')