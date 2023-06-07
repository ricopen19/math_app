import streamlit as st
# from PIL import Image, ImageOps
import numpy as np
# import cv2
# import pyocr
from gtts import gTTS
# import re
import pyttsx3
# import sys

# windowsの場合は必要、Macの場合は不要
# pyocr.tesseract.TESSERACT_CMD = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# engines = pyocr.get_available_tools()
# if len(engines) == 0:
#     print("No OCR tool found")
#     sys.exit(1)
# engine = engines[0]
col1, col2 = st.columns(2)


# def img_crop(img_view):
#     width, height = img_view.size
#     x1 = st.sidebar.slider('左上のx座標', 0, width, 0, step=int(width/100))
#     y1 = st.sidebar.slider('左上のy座標', 0, height, 0, step=int(height/100))
#     x2 = st.sidebar.slider('右下のx座標', x1 + 100, width, width, step=int(width/100))
#     y2 = st.sidebar.slider('右下のy座標', y1 + 100, height, height, step=int(height/100))
#     croped_img = img_view.crop((x1, y1, x2, y2))
#     return croped_img


# def img_bin(img_file):
#     border = st.sidebar.slider('閾値を設定してください', 0, 255, 128, step=2)
#     img_gray = img_file.convert('L').convert('RGB')
#     img_array = np.array(img_gray)
#     img_bin_array = (img_array >= border) * 255
#     img_view = Image.fromarray(img_bin_array.astype(np.uint8))
#     rev = st.sidebar.checkbox('白と黒を反転させる')
#     if rev == True:
#         img_view = ImageOps.invert(img_view)
#     return img_view


# def ocr_img(img_view):
#     builder = pyocr.builders.TextBuilder(tesseract_layout=3)
#     text = engine.image_to_string(img_view, builder=builder, lang=ocr_lang)
#     text_fixed = re.sub('([あ-んア-ン一-龥ー])\\s+((?=[あ-んア-ン一-龥ー]))', r'\1\2', text)
#     return text_fixed


def speech_gTTS(text, lang):
    gTTS(text=text, lang=lang,fast=True).save("speech.mp3")
    audio_file = open('speech.mp3', 'rb')
    col1.audio(audio_file)
    return audio_file


def speech_pyttsx3(text, voice_type):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # 言語選択
    engine.setProperty("voice", voices[voice_type].id)
    # 発話速度
    # rate = engine.getProperty('rate')
    engine.setProperty('rate', talk_speed)
    engine.save_to_file(text, "speech.aiff")
    engine.runAndWait()
    audio_file = open("speech.aiff", 'rb')
    col1.audio(audio_file)
    return audio_file


# # サイドバー
# st.sidebar.markdown('### 画像→文字出力')
# upload_image = st.sidebar.file_uploader(
#     "ファイルアップローダー", type=['jpg', 'png', 'jpeg'])
# ocr_lang = st.sidebar.selectbox("OCR化する言語を選んでください", ['jpn', 'eng'])
# ocr_button = st.sidebar.button('OCR化する')
# option_binary = st.sidebar.radio(
#     '画像を2値化しますか？（文字認識精度が改善するかもしれません）', ('しない', 'する'), horizontal=True)
# crop_option = st.sidebar.radio('画像をトリミングしますか？', ('しない', 'する'), horizontal=True)


# メインページ
col1.write('読み込んだ画像や変換した音声が表示されます')

st.markdown('#### 文章→音声出力')
st.text_area('音声化する文章を入力して下さい', key='word', height=300, placeholder='ここに入力')
onsei_button = st.button('テキストを音声化する')
option_engine = st.selectbox(
    '音声化するエンジンを選んで下さい（MacはgTTS推奨）', [
        'pyttsx3', 'gTTS'])

audio_lang = st.radio('音声化する言語を選んで下さい', ('ja', 'en'), horizontal=True)
if option_engine == 'pyttsx3':
    talk_speed = st.slider('発話速度（wpm）を設定して下さい', 60, 300, 200, step=1)


if __name__ == '__main__':
    # if upload_image is not None:
    #     img_view = Image.open(upload_image)
    #     if option_binary == 'する':
    #         img_view = img_bin(img_view)
    #     if crop_option == 'する':
    #         img_view = img_crop(img_view)

    #     st.image(img_view, caption='uploaded image', use_column_width=True)
    #     if ocr_button:
    #         txt = ocr_img(img_view)
    #         st.code(txt)

    if onsei_button:
        if option_engine == 'pyttsx3' and audio_lang == 'ja':
            speech_pyttsx3(st.session_state.word, 0)
        elif option_engine == 'pyttsx3' and audio_lang == 'en':
            speech_pyttsx3(st.session_state.word, 1)
        elif option_engine == 'gTTS':
            speech_gTTS(st.session_state.word, audio_lang)
