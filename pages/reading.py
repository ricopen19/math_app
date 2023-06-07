import streamlit as st
from gtts import gTTS

col1, col2 = st.columns(2)


def audio_replay():
    with open('speech.mp3', 'rb') as audio_file:
        audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')


def speech_gTTS(text, lang):
    gTTS(text=text, lang=lang).save("speech.mp3")
    audio_replay()


# class speech_pyttsx3:
#     def __init__(self):
#         self.engine = pyttsx3.init()
#         self.voices = self.engine.getProperty('voices')

#     def convert(self, text, voice_type, speed):
#         # 言語選択
#         self.engine.setProperty("voice", self.voices[voice_type].id)
#         # 発話速度
#         self.engine.setProperty('rate', speed)
#         self.engine.save_to_file(text, "speech.mp3")
#         self.engine.say(text)
#         self.engine.runAndWait()


st.markdown('#### 文章→音声出力')
st.text_area('音声化する文章を入力して下さい', key='word', height=300, placeholder='ここに入力')
onsei_button = st.button('テキストを音声化する')


audio_lang = st.radio('音声化する言語を選んで下さい', ('ja', 'en'), horizontal=True)


if __name__ == '__main__':

    if onsei_button:
        speech_gTTS(st.session_state.word, audio_lang)
