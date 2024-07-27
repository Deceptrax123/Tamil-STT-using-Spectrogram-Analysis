import librosa
import numpy as np
import matplotlib.pyplot as plt
from statistics import NormalDist
from scipy.ndimage import maximum_position as extract_region_maximums
from scipy.ndimage import label


def plot_peaks(peaks):
    plt.scatter(
        x=[p[0] for p in peaks],
        y=[p[1] for p in peaks],
        s=1.5,
        color='blue'
    )

    plt.show()


def peak_finding(s):
    spectrogram = s
    threshold = 3.75

    flattened = np.matrix.flatten(spectrogram)
    filtered = flattened[flattened > np.min(flattened)]

    ndist = NormalDist(np.mean(filtered), np.std(filtered))

    zscore = np.vectorize(lambda x: ndist.zscore(x))
    zscore_matrix = zscore(spectrogram)

    mask_matrix = zscore_matrix > threshold
    labelled_matrix, num_regions = label(mask_matrix)
    label_indices = np.arange(num_regions)+1

    peak_positions = extract_region_maximums(
        zscore_matrix, labelled_matrix, label_indices)

    peaks = [(x, y, spectrogram[y, x]) for y, x in peak_positions]

    # plot_peaks(peaks)

    return peaks
