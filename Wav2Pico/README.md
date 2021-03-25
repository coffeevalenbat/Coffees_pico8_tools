# Wav file to Pico-8 sample format (By JWinslow23)
To run this script, you'll first need a few things:
-xclip package
-replace line 37 to match where your Pico-8 excecutable is located.
-Python 3
-Librosa and argparse extensions for Python 3

After that, do something like ```./Wav2P8.sh name_of_your_sample.wav``` , this will outṕut either a .txt file with your sample or copy it to your 
clipboard, depending on what you choose within the script.
You can also add anything as a 2nd argument to instead output a cart with your sample and the sample player code already written in.
