import streamlit as st
import pandas as pd
import numpy as np


dataframe = pd.DataFrame(np.random.randn(5,20))
data = pd.DataFrame(np.random.randn(20,3), columns=["a","b","c"])

st.title("Green Q") #タイトル
st.write("GreenQへようこそ！　このサイトはサンプルです。") # 表示

check = st.checkbox("累積の表示") # チェックボタン

if check:
 st.dataframe(dataframe) #pandasのデータフレーム
 st.table(dataframe) # 静的な表
 st.metric(label="Temperature", value="70 °F", delta="1.2 °F") #指標

 st.line_chart(dataframe) #線グラフ
 st.area_chart(dataframe) #チャート
 st.bar_chart(dataframe) #棒グラフ