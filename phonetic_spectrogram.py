import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy


def remove_silence(audio_path, top_db=30):
    audio, sr = librosa.load(audio_path, sr=None)
    non_silent_intervals = librosa.effects.split(audio, top_db=top_db)
    audio_no_silence = np.concatenate(
        [audio[start:end] for start, end in non_silent_intervals])
    return audio_no_silence, sr


def pre_emphasis(signal, pre_emphasis_coefficient=0.97):
    emphasized_signal = np.append(
        signal[0], signal[1:] - pre_emphasis_coefficient * signal[:-1])
    return emphasized_signal


def compute_spectrogram_and_find_peaks(audio_path):
    # Remove silence
    audio_no_silence, sr = remove_silence(audio_path)

    # Apply pre-emphasis filter
    emphasized_signal = pre_emphasis(audio_no_silence)

    # Compute the Short-Time Fourier Transform (STFT)
    S = librosa.stft(emphasized_signal)

    # Convert amplitude to decibels
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    return S_db
