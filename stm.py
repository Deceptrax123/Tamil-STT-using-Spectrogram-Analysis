import librosa
import numpy as np
import matplotlib.pyplot as plt


def mfcc(frames, i, band_index):
    mfcc_stm = librosa.feature.mfcc(
        y=frames[i][band_index:], sr=16000, n_mfcc=12, hop_length=10, win_length=25)

    return mfcc_stm


def a(i, frames, v, I=3):
    result = 0
    sum_sq_j = 28

    for j in range(-I, I):  # mfcc around frame i
        if i+j >= len(frames):
            break
        result += mfcc(frames, j+i, v)*j

    a = result/sum_sq_j

    return a


def C(a_i):
    result_i = a_i**2

    return result_i


def process(path):
    audio, sr = librosa.load(
        path, sr=16000)

    frames = librosa.util.frame(audio, frame_length=25, hop_length=10)
    windowed = np.hanning(25).reshape(-1, 1)*frames

    # mfcc of each frame i
    for i, frame in enumerate(windowed):

        frame_emphasised = librosa.effects.preemphasis(frame)

        # extract mel coefficients
        mfcc_frame = librosa.feature.mfcc(
            y=frame_emphasised, sr=sr, n_mfcc=12, hop_length=10, win_length=25)

        for v in range(12):
            a_i = a(i, frame_emphasised, v)  # find the function C
            c_i += C(a_i)

        stm = c_i/(v+1)

        print(stm.shape)


if __name__ == '__main__':
    process("/Volumes/Vault/Smudge/Datasets/Tamil/Wav-Audios/1audio.wav")
