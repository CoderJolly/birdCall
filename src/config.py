import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))[:-4] # [-4] is done to remove /src
AUDIODATA_DIR = os.path.join(ROOT_PATH,'data/1_audio_data')
DENOISE_DIR = os.path.join(ROOT_PATH, 'data/2_denoise_data')
RESULT_DIR = os.path.join(ROOT_PATH, 'data/3_chunk_data')
PITCH_DIR = os.path.join(ROOT_PATH, 'data/4_pitch_change')
TIME_DIR = os.path.join(ROOT_PATH, 'data/5_time_change')
MEL_DIR = os.path.join(ROOT_PATH, 'results/6_mel_result')
MFCC_DIR = os.path.join(ROOT_PATH, 'results/7_mfcc_result')

print(ROOT_PATH, AUDIODATA_DIR)