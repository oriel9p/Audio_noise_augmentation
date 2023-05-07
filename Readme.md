## Audio augmentation with noise file

a simple python script for augmenting audio files (.wav) with an existing noise file.

### Setup
1. Import dependencies

math, os, numpy, random, pydub (AudioSegment)

2. Change path to files and noise file
directory_path = "\your\path\to\files"
noise_file_path = "\your\path\to\noise"

3. Set target SNR
target_snr = 10

4. Run the file

