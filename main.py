import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


# df = pd.DataFrame({
#     '001': [1, 2, 3, 4],
#     '002': [10, 20, 30, 40]
# })
# df = pd.DataFrame(
#     np.random.randint(0, 100, size=(20, 3)),
#     columns = ['a', 'b', 'c']
# )
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)
df2 = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)

st.title('jaja')

bar_num = st.empty()
bar = st.progress(0)
for i in range(100):
    bar_num.text(f'Iteration: {i+1}')
    bar.progress(i+1)
    time.sleep(.1)

# condition = st.slider('condition', 0, 100, 50)
# 'condition: ',condition 
# txtinput = st.text_input('hobby')
# 'hobby: ', txtinput, 'ja.'

# condition = st.sidebar.slider('condition', 0, 100, 50)
# 'condition: ',condition 
# txtinput = st.sidebar.text_input('hobby')
# 'hobby: ', txtinput, 'ja.'

lcolumn, rcolumn = st.beta_columns(2)
btn = lcolumn.button('btn')
if btn:
    rcolumn.write('display')

q1 = st.beta_expander('question1')
q1.write('answer1')
q2 = st.beta_expander('question2')
q2.write('answer2')
q3 = st.beta_expander('question3')
q3.write('answer3')
q4 = st.beta_expander('question4')
q4.write('answer4')

condition = st.sidebar.slider('condition', 0, 100, 50)
'condition: ',condition 
txtinput = st.sidebar.text_input('hobby')
'hobby: ', txtinput, 'ja.'

option = st.selectbox(
    'number',
    list(range(1, 9))
)
'number: ',option,

if st.checkbox('show', True):
    img = Image.open('../../img/cat.png')
    st.image(img, caption='mew', use_column_width=True)

st.write('DateFrame')
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.map(df2)

# st.write(df)
# st.dataframe(df, width=640, height=360)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as no
# import pandas as pd
# ```
# """
