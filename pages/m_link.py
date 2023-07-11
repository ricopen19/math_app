import streamlit as st


def make_link(link, title):
    for link, title in zip(link, title):
        st.markdown(f"<a href={link}>{title}</a>", unsafe_allow_html=True)


st.markdown('#### 数学を勉強して身につく力')

power_link = [
                'https://www.iot-makers.co.jp/blog/column/1857/',
                'http://xn--h9jua5ezakf0c3qner030b.com/11785.html',
]

power_title = ['数学は必要ないと思っていませんか？？',
               'チコちゃんクイズ「なんで数学を勉強するの？」',
               ]

make_link(power_link, power_title)


st.markdown('#### 数学教育について')

edu_link = [
        'https://toyokeizai.net/articles/-/475479',
        'https://toyokeizai.net/articles/-/413252',
        'https://toyokeizai.net/articles/-/278180',
        'https://swing-jyuku.jp/method/子育て/recommendation-of-mathematics/',

]

edu_title = [
        '「数学嫌い」の人は暗記教育の犠牲者と言える理由',
        '「数学嫌いの若者」が生み出され続ける根本原因',
        '大学生が「%」がわからない日本の絶望的な現実',
        '「数学なんて、将来使わないから勉強しないよ」に何と答える？',
]

make_link(edu_link, edu_title)


st.markdown('#### 個人について')

personal_link = [
        'https://jp.quora.com/数学は将来役に立たない-という意見にどう反論しま',
        'https://nie.hokkaido-np.co.jp/nayami/93/',
]

personal_title = [
        '「数学は将来役に立たない」という意見にどう反論しますか',
        '悩みごとナビ「数学を学ぶ必要性感じません」',
]

make_link(personal_link, personal_title)


st.markdown('#### 進学について')

st.markdown("<a href='https://sky-yobiko.net/humanities-math-dispose-of/'>私立文系は数学捨てるべき？私文系数学が必要な理由を知って後悔しない！</a>", unsafe_allow_html=True)



st.markdown('#### 需要について')

demand_link = [
        'https://www.tac-school.co.jp/tacnewsweb/feature/feat202001_1.html',
        'https://www.su-gaku.net/others/mathematical_innovation/',
        'https://xtech.nikkei.com/atcl/nxt/column/18/00138/052100282/',
        'https://toyokeizai.net/articles/-/475479',
        'https://www.toyo.ac.jp/link-toyo/life/economics_math/'
]

demand_title = [
        'いま、ビジネスに「数学」が必要なワケ',
        '急速に進む「数学」需要──数理イノベーション時代の到来',
        '文系（プログラマー）を悩ます「これからは数学が大事」論',
        '早稲田政経が粉砕「数学不要論」の先にある大革命',
        '文系だから数学は不要？教員が語る、経済学と数学の強い結びつきとは'
]

make_link(demand_link, demand_title)

st.markdown('#### 林先生特集')

h_link = [
        'https://sirabee.com/2021/03/29/20162543714/',
        'https://rikeiya.com/sugakuttehitsuyo/hayashi-osamu',
        'https://depalma01.com/2020/01/08/hayashi-math/',
        'https://www.mbs.jp/mbs-column/mimi/archive/2019/04/28/016953.shtml',
        ]

h_title = [
        '林修先生、現代文講師ながら「国語より算数が好き」　その理由は… – Sirabee',
        '林修「学校の勉強の中で、圧倒的に大事なのは数学」 | 理系屋',
        '林修先生の名言『数学の考え方は日常生活で役に立つ』【人生論・できない】 | 作家になるためのシステム',
        '林修・その数字の意味、考えてますか？視力に1.1がない理由 | 日曜日の初耳学 復習編 | MBSコラム',
        ]

for link, title in zip(h_link, h_title):
    st.markdown(f"<a href={link}>{title}</a>", unsafe_allow_html=True)
