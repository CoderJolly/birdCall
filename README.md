# Bird Species Classification Using Bird Call Recordings
- Birds play an essential role in nature. They are high up in the food chain and integrate changes occurring at lower levels. Birds are excellent indicators of deteriorating habitat quality and environmental pollution. 
- They are  significant in determining the aspects of our nature and to intuit factors about an area’s quality of life based on a changing bird population. With proper sound detection and classification, researchers can understand what birdcall signal these birds use, in order to communicate with each other or to warn others about the impending dangers in the vicinity.
- However, it is easier to hear birds than see them and hence audio classification plays a vital role than video or picture based monitoring. Data science may be able to assist, so researchers have turned to large crowd sourced databases of focal recordings of birds to train AI models. 

# Directory Structure

-  **[1_audio_data](https://github.com/teambirdcall/birdcall/tree/main/1_audio_data)** - Contains the raw Audio files categorized by their species name as folders. This folder should contain the original audios that have not been chunked and are of variable length.

-  **[2_denoise_data](https://github.com/teambirdcall/birdcall/tree/main/2_denoise_data)** - Contains the denoised raw Audio files categorized by their species name as folders.

-  **[3_chunk_data](https://github.com/teambirdcall/birdcall/tree/main/3_chunk_data)** - It contains the chunked audios as per respective species folder that have been made from audiodata folder.

-  **[4_pitch_change](https://github.com/teambirdcall/birdcall/tree/main/4_pitch_change)** - It contains the pickle files of each respective species that have changed on the basis of pitch and dumped in this folder.

-  **[5_time_change](https://github.com/teambirdcall/birdcall/tree/main/5_time_change)** - It contains the pickle files of each respective species that have changed on the basis of time and dumped in this folder.

-  **[6_mel_result](https://github.com/teambirdcall/birdcall/tree/main/6_mel_result)**- It contains the mel-spectrogram of chunked audios as per respective species that have been made from result folder.

-  **[7_mfcc_result](https://github.com/teambirdcall/birdcall/tree/main/7_mfcc_result)** - It contains the mfcc-data in the form of pickle files of all the species in the result folder.
