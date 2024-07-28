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

## Running the current version
1. **Clone the GitHub Repository**:
   Clone the repository using SSH:
   ```sh
   git clone git@github.com:Deceptrax123/Tamil-STT-using-Spectrogram-Analysis.git
   ```
2. Create and activate a virtual environment and run
    ```sh
    pip install -r requirements.txt
    ```
3. Download the audio files comprising the syllables
4. Record the Tamil transcription on your device and save it as a ```.mp3``` or ```.wav``` file.
5. Edit the ```speech_to_text.py``` script to set the audio path to your source file.
6. Run
   ```sh
   python speech_to_text.py
    ```
## File Description
|File Name|Description|
|----------|----------|
|```peaks.py```|Find the peaks of the spectrogram|
|```speech_to_text.py```|Convert the speech recorded in Tamil to Tamil Phonetic Sound|
|```phonetic_spectrogram.py```|Get the spectral features of the 247 Tamil Characters|
|```stm.py```|Source for Spectral Transition Measure(Under Development)|
|```tamil_phonetic.json```|Mapping of Tamil characters to its corresponding audo files|

## Collaborators
| [<img src="https://github.com/Kriticle.png?size=50" width="50"/>](https://github.com/Kriticle)| [<img src="https://github.com/VaishnaviDixit14.png?size=50" width="50"/>](https://github.com/VaishnaviDixit14) | [<img src="https://github.com/DARKSNOUT.png?size=50" width="50"/>](https://github.com/DARKSNOUT) | [<img src="https://github.com/Deceptrax123.png?size=50" width="50"/>](https://github.com/Deceptrax123) |
| -------- | -------- | -------- | -------- |
