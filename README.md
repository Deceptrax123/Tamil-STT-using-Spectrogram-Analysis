# Tamil Speech to Text using Spectrogram Analysis
Prototype Solution of transcribing Tamil speech to phonetic sounds in the Tamil language.

## Approach to the Problem
  - Pre-processing of audio using Centroid Estimation for silence removal.
  - Wave correction through L1 Formant Analysis using a Linear Predictor Method wih an initial parameter p 
  - Short time fourier transform of the corrected waveform to convert the signals from time to frequency domain
  - Plotting a spectrogram of the audio signal and finding local and global peaks of the waveform
  - Average filter is passed into the corrected waveform to account for spurious peaks.
  - Segment the audio keeping peaks as boundary points and map the spectral signatures of the segmented audio to the nearest spectral features of the Tamil phonetic sound.
  - Display the phonetic sounds as Tamil characters.

## File Description
|File Name|Description|
|----------|----------|
|```peaks.py```|Find the peaks of the spectrogram|
|```speech_to_text.py```|Convert the speech recorded in Tamil to Tamil Phonetic Sound|
|```phonetic_spectrogram.py```|Get the spectral features of the 247 Tamil Characters|
|```stm.py```|Source for Spectral Transition Measure(Under Development)|

## Collaborators
