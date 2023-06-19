import streamlit as st
from pages import m_link

st.markdown('# :green[トップページ] :100: #')

f_link = [
    'https://onl.bz/RZCi55J',
          ]

f_title = [
    '6/9（金）　小テスト 数Ⅱ（点と直線、直線の方程式）',
    ]

m_link.make_link(f_link, f_title)