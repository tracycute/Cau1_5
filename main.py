import streamlit as st
import numpy as np
import pandas as pd

st.title('My frist deployed DL model')
st.header('Header đây chớ đâu')
st.text('Đây là text')
st.markdown('Markdown đây **anh em ơi**')
st.write('Còn dưới đây là latex')
st.latex(r'''a + b = 3 ''')
st.write(12345)
st.code('''def(hello):
        print("Hello world!")
        ''', language='python', line_numbers = True)
st.text('Hiển thị luôn cả chart')
data = np.random.randn(20, 3)
df = pd.DataFrame(data, columns = ['a', 'b', 'c'])
st.line_chart(df)

#https://21520255-cau-1-5.streamlit.app/
