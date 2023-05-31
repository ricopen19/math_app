import streamlit as st


st.markdown('# :green[トップページ] :100: #')

st.title('三角関数')
st.latex('sinθ^2 + cosθ^2 = 1')
st.latex('sin(α±β) = sinαcosβ ± cosαsinβ')

link = 'https://www.geogebra.org/m/pe2sknyk'
st.markdown(' **_GeoGebra_** ')
st.markdown(f'<a href="{link}">三角関数の値</a>', unsafe_allow_html=True)