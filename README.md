## Bird Species Classification Using Bird Call Recordings
- Birds play an essential role in nature. They are high up in the food chain and integrate changes occurring at lower levels. Birds are excellent indicators of deteriorating habitat quality and environmental pollution. 
- They are  significant in determining the aspects of our nature and to intuit factors about an area’s quality of life based on a changing bird population. With proper sound detection and classification, researchers can understand what birdcall signal these birds use, in order to communicate with each other or to warn others about the impending dangers in the vicinity.
- However, it is easier to hear birds than see them and hence audio classification plays a vital role than video or picture based monitoring. Data science may be able to assist, so researchers have turned to large crowd sourced databases of focal recordings of birds to train AI models. 


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

## Directory Structure

-  **[1_audio_data](https://github.com/teambirdcall/birdcall/tree/main/1_audio_data)** - Contains the raw Audio files categorized by their species name as folders. This folder should contain the original audios that have not been chunked and are of variable length.

-  **[2_denoise_data](https://github.com/teambirdcall/birdcall/tree/main/2_denoise_data)** - Contains the denoised raw Audio files categorized by their species name as folders.

-  **[3_chunk_data](https://github.com/teambirdcall/birdcall/tree/main/3_chunk_data)** - It contains the chunked audios as per respective species folder that have been made from audiodata folder.

-  **[4_pitch_change](https://github.com/teambirdcall/birdcall/tree/main/4_pitch_change)** - It contains the pickle files of each respective species that have changed on the basis of pitch and dumped in this folder.

-  **[5_time_change](https://github.com/teambirdcall/birdcall/tree/main/5_time_change)** - It contains the pickle files of each respective species that have changed on the basis of time and dumped in this folder.

-  **[6_mel_result](https://github.com/teambirdcall/birdcall/tree/main/6_mel_result)**- It contains the mel-spectrogram of chunked audios as per respective species that have been made from result folder.

-  **[7_mfcc_result](https://github.com/teambirdcall/birdcall/tree/main/7_mfcc_result)** - It contains the mfcc-data in the form of pickle files of all the species in the result folder.

![directory-struct](/figures/directory-struct.png)


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

