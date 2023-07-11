import streamlit as st

st.title('三角関数の応用例')

f_link = [
    'https://time-space.kddi.com/ict-keywords/kaisetsu/20160427',
    'https://www.youtube.com/watch?v=3Bvcx_qBLHQ&list=PL42xVavpwPn4cM4SQDiRast9ZH75f5SdB',
    'https://togetter.com/li/1890846',
    'https://www.nicovideo.jp/watch/sm13283644'
    'https://www.nicovideo.jp/watch/sm30542522'

          ]

f_title = [
    '騒音だけなぜ消える？ 『ノイズキャンセリング』の仕組みとは｜KDDI トビラ',
    '東大数学科のアドバイス：サインもコサインも円で考えよう【好きになっちゃう放課後】',
    '「三角関数まじパネエな」「なくしたら世の中のゲームの９割が消滅する」ゲームプログラムでみる三角関数の有用性',
    '声(母音)は三角関数(sin)の足し算で簡単に作れます',
    '【合成音声】 MIDIに歌わせてみた 【小林さんちのメイドラゴン OP】'
    ]


for link, title in zip(f_link, f_title):
    st.markdown(f"<a href={link}>{title}</a>", unsafe_allow_html=True)