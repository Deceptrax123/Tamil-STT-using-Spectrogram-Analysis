# Tamil Speech to Text using Spectrogram Analysis
Prototype Solution of transcription of  Tamil speech to phonetic sounds in the Tamil language.

## Approach to the Problem
1. **Silence Removal via Centroid Estimation**: Pre-process the audio signal to remove silence by estimating the centroid.
2. **Wave Correction through L1 Formant Analysis**: Apply L1 formant analysis using a linear predictor method with an initial parameter \( p \) to correct the waveform.
3. **Time-Frequency Domain Conversion**: Perform a Short-Time Fourier Transform (STFT) on the corrected waveform to convert the signals from the time domain to the frequency domain.
4. **Spectrogram Analysis**: Generate a spectrogram of the audio signal and identify both local and global peaks within the waveform.
5. **Peak Smoothing**: Apply an average filter to the corrected waveform to mitigate spurious peaks.
6. **Audio Segmentation and Mapping**: Segment the audio signal using identified peaks as boundary points. Map the spectral signatures of the segmented audio to the closest spectral features of Tamil phonetic sounds.
7. **Phonetic Sound Display**: Convert the mapped spectral features into Tamil characters to display the corresponding phonetic sounds.


## File Description
|File Name|Description|
|----------|----------|
|```peaks.py```|Find the peaks of the spectrogram|
|```speech_to_text.py```|Convert the speech recorded in Tamil to Tamil Phonetic Sound|
|```phonetic_spectrogram.py```|Get the spectral features of the 247 Tamil Characters|
|```stm.py```|Source for Spectral Transition Measure(Under Development)|

## Collaborators
