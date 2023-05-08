## Bird Species Classification Using Bird Call Recordings
- Birds play an essential role in nature. They are high up in the food chain and integrate changes occurring at lower levels. Birds are excellent indicators of deteriorating habitat quality and environmental pollution. 
- They are  significant in determining the aspects of our nature and to intuit factors about an area’s quality of life based on a changing bird population. With proper sound detection and classification, researchers can understand what birdcall signal these birds use, in order to communicate with each other or to warn others about the impending dangers in the vicinity.
- However, it is easier to hear birds than see them and hence audio classification plays a vital role than video or picture based monitoring. Data science may be able to assist, so researchers have turned to large crowd sourced databases of focal recordings of birds to train AI models. 

## Directory Structure
```
├── data/                       <- Audio files for the project
|  ├── 1_audio_data/            <- Contains the raw Audio files
|  ├── 2_denoise_data/          <- Contains the denoised raw Audio files
|  ├── 3_chunk_data/            <- Contains the chunked audios after denoising them
|  ├── 4_pitch_change/          <- Contains augmented audios after changing pitch
|  ├── 5_time_change/           <- Contains augmented audios after changing time
├── figures/                    <- Figures used in README
├── src/                        <- Source code for the project
│  ├── __init__.py              <- Makes src a Python module
│  ├── audio_denoising.py       <- Denoising the raw audio files
│  ├── config.py                <- Makes paths for automating the pre-processing pipeline
│  ├── config.json              <- Configuration file for the model
│  ├── data_utils.py            <- Initialized utility functions for handling the data before model training
|  ├── model_utils.py           <- Initialized model and training functions
│  ├── preprocess_utils.py      <- Initialized utility functions for preprocessing the audio data
|  ├── run_model.py             <- Calling all functions to run the model (fitting and evaluation)
|  ├── run_preprocess_utils.py  <- Calling all functions to run the preprocessing pipeline
├── results/                    <- Feature extration done on the audio files (Melspectograms and MFCCs)
|  ├── 6_mel_result/            <- Contains the Mel Spectrograms made wile processing the audio files
├── .gitignore                  <- List of files and folders git should ignore
├── LICENSE                     <- Project's License
└── README.md                   <- The top-level README for developers using this project
```

![directory-struct](/figures/directory-struct.png)

## Exploratory Data Analysis
- After screening the Cornell data, we can see that from the year 2012, a vast majority of sample counts started to be recorded up until 2019. The year 2014 saw a significant rise in the number of recorded samples also the highest sample recordings amongst all years.
![eda-year](/figures/eda-year.png)

- The top 5 song types have been also listed wherein they include whether the audio was a bird song or a bird-call. There are mentions of flight call and call song as well, which are nearly of the same number.
![eda-song](/figures/eda-song.png)

- This waveplot for the bird species, American Woodcock shows a leveled amplitude and speed with sampling rate of 16 Khz with a peent sound (nasal sound by amewoo) around 23 seconds long.
![eda-wavelet](/figures/eda-wavelet.png)

- For the same species, we can see an increasing and decreasing amplitude but a leveled speed with sampling rate of 48 Khz with a flight call. It is a stereo audio around 8 seconds long.
![eda-amplitude](/figures/eda-amplitude.png)

## Data Preprocessing

- ### Chunking
     The Cornell dataset and the Xeno-Canto dataset have inconsistent length audios, so a fixed sized input for model is needed. Therefore, I made chunks of 5 seconds each and for the variable difference, a padding of silence is added in the last to keep the chunk size constant throughout.

- ### Data Augmentation
    Limited by the number of audio samples per class in the Xeno-Canto dataset, data augmentation became imperative. I applied two data augmentation techniques that are Pitch Shift and Time Shift. Both of these techniques force the network to deal with irregularities in the spectrogram and also, more importantly, teach the network that bird songs/calls appear at any time, independent of the bird species. 

## Feature Extraction

The aim of feature extraction is to compress the audio signals into a distinct form that characterises the important information of each sound event. As a result, classification procedures are based on feature extraction. Mel Spectrograms and Mel-frequency Cepstrum Coefficients (MFCC) are two feature extraction methods often used in audio-related projects.
- Mel spectrogram is a spectrogram that uses a mel scale on the y axis. Mel scale is the perceived frequency. Human ears convert the measured frequency to a human audible  and that is known as perceived frequency.
- The MFCC feature extraction technique basically includes windowing the signal, applying the DFT, taking the log of the magnitude, and then wrapping the frequencies on a Mel scale, followed by applying the  DCT.
- Before calculating Mel-frequency Cepstrum Coefficients and Mel values, the audios were chunked into 5-second recordings  to reduce the size of the file.

![melspec](/figures/melspec.png)

## Model: CNN

By just listening to the audios, we cannot perceive much information from it, but if sound frequencies could be turned into images and then those images be used to extract features in some manner and we might be able to understand a larger range of frequencies.

Thus, I chose CNNs for audio classification, as they work best for image classification, and what we are feeding to our model is an image i.e. Mel Spectrograms.

![model-cnn](/figures/model-cnn.png)

## Credits
- [Dr. Sarabjot Anand](https://www.bmu.edu.in/faculty/dr-sarabjot-singh-anand/)
- [Anish Sachdeva](https://github.com/anishLearnsToCode)

