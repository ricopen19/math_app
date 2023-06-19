from gensim.models.word2vec import Word2Vec
import streamlit as st

model_path = './model/word2vec.gensim.model'
model = Word2Vec.load(model_path)
# words = model.wv.most_similar('東京')

# words = model.wv.most_similar(positive=['東京', '自然'], negative=['都会'])

# for word in words:
#     print(word)


st.title('単語計算アプリ')

word1 = st.text_input('単語1')

word2 = st.text_input('単語2')

# word3 = st.text_input('入力3')

ope1 = st.radio('計算1', ('+', '-'))


st.markdown('#### 計算式')
st.code(f'「{word1}」　{ope1}　「{word2}」')

positive = []
negative = []
if ope1 == '+':
    positive.append(word1)
    positive.append(word2)

else:
    positive.append(word1)
    negative.append(word2)

if st.button('計算'):
    words = model.wv.most_similar(positive=positive, negative=negative)
    for word in words:
        st.write(words)
    
