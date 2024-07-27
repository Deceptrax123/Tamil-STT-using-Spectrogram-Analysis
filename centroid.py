import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy
from peaks import peak_finding
import math


def plot_centroid(centroid, frame):
    S = librosa.amplitude_to_db(librosa.magphase(
        librosa.stft(y=frame))[0], ref=np.max)
    times = librosa.times_like(centroid)

    fig, ax = plt.subplots()
    librosa.display.specshow(S, y_axis='log', x_axis='time', ax=ax)
    ax.plot(times, centroid.T, label='Spectral Centroid', color='w')
    ax.legend(loc='upper right')
    ax.set(title='Spectrogram')

    plt.show()


def plot_autocorrelation(frame, y_hat):
    fig, ax = plt.subplots()
    ax.plot(frame)
    ax.plot(y_hat, linestyle='--')
    ax.legend(['x(n)', 'xhat_n'])
    ax.set_title("LP Foward Prediction")
    plt.show()


def plot_corrected(s, sr=16000):
    S = librosa.amplitude_to_db(np.abs(s), ref=np.max)
    fig = plt.figure()
    img = librosa.display.specshow(
        S, x_axis='time', y_axis='log', sr=sr, hop_length=512, n_fft=1024)
    plt.title("Corrected Spectrogram")

    fig.colorbar(img, format="%+2.f dB")

    plt.show()


def process(path):
    audio, sr = librosa.load(
        path, sr=16000)

    frames = librosa.util.frame(audio, frame_length=10, hop_length=2)
    windowed = np.hanning(10).reshape(-1, 1)*frames

    # get spectral centroid for each frame
    for i, frame in enumerate(windowed):
        centroid = librosa.feature.spectral_centroid(
            y=frame, sr=sr, n_fft=1024, win_length=1024, hop_length=512)
        # plot_centroid(centroid, frame)

        # Perform Formant Analysis
        p = round(16000/1000)+2
        lpc_coeff = librosa.lpc(y=frame, order=p)

        # Autocorrelation to remove erroneous signals
        b = np.hstack([[0], -1*lpc_coeff[1:]])
        y_hat = scipy.signal.lfilter(b, [1], frame)

        plot_autocorrelation(frame=frame, y_hat=y_hat)

        # find spectral features in the F1 Domain
        y_hat = librosa.decompose.nn_filter(S=y_hat, aggregate=np.average)
        s, phase = librosa.magphase(librosa.stft(
            y_hat, n_fft=1024, hop_length=512))

        plot_corrected(s)

        # find peaks
        peaks = peak_finding(s)
        print(peaks)


if __name__ == '__main__':
    process("/Volumes/Vault/Smudge/Datasets/Tamil/Wav-Audios/1audio.wav")