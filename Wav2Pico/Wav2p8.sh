#!/bin/sh
# Syntax for this script:
# ./Wav2p8.sh Sample_filename (Add a second parameter if you want full p8 cart mode)
name=$(echo "$1" | cut -f 1 -d '.')

clipb(){
   xclip -sel c < $name.txt
   exit
}

fle(){
   gedit $name.txt
   exit
}

pick_standalone(){
      while true; do
      read -p "Copy to clipboard or open file?(C/F)" cf
      case $cf in
         [Cc]* ) clipb break;;
         [Ff]* ) fle break;;
         * ) echo "Cmon dude";;
      esac
   done
}

standalone()
{
mv temp.txt $name.txt
pick_standalone
}

full_cart()
{
sed "s/yoursamplehere/$(cat temp.txt)/" stuff/main_pcm.p8 > $name.p8
rm temp.txt
~/pico-8/pico8 $name.p8
}

if [ -z "$2" ]
then
   echo "Standalone text file mode"
python3 stuff/w2p8.py $1
	standalone
else
   echo "Full p8 mode"
python3 stuff/w2p8.py $1
	full_cart
fi