import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg


sample_rate = 44100
# 再生時間を指定
seconds = 1

# 時間軸の作成
time = np.arange(sample_rate * seconds) / sample_rate


# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)

# y = y.astype(np.int16)
# xseconds = x/44100
# plt.plot(xseconds,y)
# plt.xlim(0,0.1)
# sound_arr = y.reshape(int(y.shape[0]/2), 2)


def wav_to_sound(wav, freq):
    if wav == 'サイン波':
        sound = np.sin(2 * np.pi * freq * t)
        # sample = np.sin(np.arange(sample_rate) * freq * np.pi * 2 / sample_rate)
    elif wav == '矩形波':
        sound = sg.square(2 * np.pi * freq * t) 
    elif wav == 'ノコギリ波':
        sound = sg.sawtooth(2 * np.pi * freq * t)
        # クリッピングしきい値
        # threshold = 0.001

        # クリッピングを適用した音声信号
        # sound = np.clip(sound, -threshold, threshold)
    elif wav == '三角波':
        sound = sg.sawtooth(2 * np.pi * freq * t, width=0.5)   
    else:
        sound = 0 * np.sin(2 * np.pi * freq * t)
    return sound

wav_form1 = st.sidebar.radio('波形1を選んでください', ('サイン波', '矩形波', 'ノコギリ波', '三角波'), horizontal=True)
freq1 = st.sidebar.slider('周波数を入力してください(Hz)', 110, 1320, value=440, step=10, key='freq1')
sound1 = wav_to_sound(wav_form1, freq1)
# 音を再生
st.sidebar.audio(sound1, sample_rate=sample_rate)

wav_form2 = st.sidebar.radio('波形2を選んでください', ('サイン波', '矩形波', 'ノコギリ波', '三角波', '表示しない'), horizontal=True)
freq2 = st.sidebar.slider('周波数を入力してください(Hz)', 110, 1320, value=440, step=10, key='freq2')
sound2 = wav_to_sound(wav_form2, freq2)
st.sidebar.audio(sound2, sample_rate=sample_rate)

st.write('波形1、2の合成波')
st.audio(sound1+sound2, sample_rate=sample_rate)

fig, ax = plt.subplots(figsize=(6,3))
ax.plot(time[:441], sound1[:441], label='wave1')
ax.plot(time[:441], sound2[:441], label='wave2')
ax.plot(time[:441], sound1[:441] + sound2[:441], label='wave1+2')
ax.grid()
ax.legend(loc="upper right")
ax.set_xlabel('Time [s]')
st.pyplot(fig)
