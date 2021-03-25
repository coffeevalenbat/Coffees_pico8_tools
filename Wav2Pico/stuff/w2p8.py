# PICO-8 Sample converter by JWinslow23, edited by Coffeebat
import librosa
import pyperclip
import argparse

# huge P8SCII table
P8SCII = ["\\000", "¹","²","³","⁴","⁵","⁶","⁷","⁸","\\t","\\n","ᵇ","ᶜ","\\r","ᵉ","ᶠ","▮","■","□","⁙","⁘","‖","◀","▶","「","」","¥","•","、","。","゛","゜"," ","!","\\\"","#","$","%","&","'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","𝘢","𝘣","𝘤","𝘥","𝘦","𝘧","𝘨","𝘩","𝘪","𝘫","𝘬","𝘭","𝘮","𝘯","𝘰","𝘱","𝘲","𝘳","𝘴","𝘵","𝘶","𝘷","𝘸","𝘹","𝘺","𝘻","[","\\\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~","○","█","▒","🐱","⬇️","░","✽","●","♥","☉","웃","⌂","⬅️","😐","♪","🅾️","◆","…","➡️","★","⧗","⬆️","ˇ","∧","❎","▤","▥","あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん","っ","ゃ","ゅ","ょ","ア","イ","ウ","エ","オ","カ","キ","ク","ケ","コ","サ","シ","ス","セ","ソ","タ","チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ","ヒ","フ","ヘ","ホ","マ","ミ","ム","メ","モ","ヤ","ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン","ッ","ャ","ュ","ョ","◜","◝"]

# argument parser
parser = argparse.ArgumentParser(description="Convert .wav files to sampled audio")
parser.add_argument("file",
	help=".wav file to convert"
)
parser.add_argument("-b",
	default=8,
	type=int,
	choices=range(1,9),
	metavar="[1..8]",
	help="bit depth to convert to (default: %(default)s)"
)
parser.add_argument("-n",
	action="store_true",
	help="if present, normalize before converting (recommended)"
)

args = parser.parse_args()

# load audio at 5512Hz
y, sr = librosa.load(args.file, sr=5512)

# normalize
if args.n:
	y = librosa.util.normalize(y)

# bring samples to correct range
amp = pow(2, args.b - 1) - .5 # -.5 to clamp between 0 and 2^n-1 instead of 0 and 2^n
samples = [int(round(s * amp + amp)) for s in y]

print("{} samples converted.".format(len(samples)))
if len(samples) > 32767:
	print("WARNING: sample size exceeds max integer")

# create bitstring
sample_str = "".join("{{:0{}b}}".format(args.b).format(s) for s in samples)
sample_str += "0" * (len(sample_str) % 8)

# convert to P8SCII
sample_str = "".join(P8SCII[int(b, 2)] for b in [sample_str[i:i+8] for i in range(0, len(sample_str), 8)])

print("Encoded into string of length {}.".format(len(sample_str)))
if len(sample_str) > 32767:
	print("WARNING: string length exceeds max string length")

# pyperclip.copy('{{b={},n={},s="{}"}}'.format(args.b, len(samples), sample_str))
file1 = open("temp.txt","w") 
final_string='{{b={},n={},s="{}"}}'.format(args.b, len(samples), sample_str)
file1.write(final_string)

filefix = open("temp.txt","rt")
data = filefix.read()
data = data.replace('\\', '○')
filefix.close()
filefix = open("temp.txt", "wt")
filefix.write(data)
filefix.close()

print("Sample string saved to file.")
