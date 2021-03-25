# Font tool (By Zep)
To run this, load the font_snippet.p8 file and export the spritesheet with something like ```export font.png```,
Then edit the image on your favorite software, save it back to the original file and in Pico-8 after loading up the font cart once again, do ```import font.png```.
After that, run the cart and a file named "font.lua.p8l" should pop up on the same folder as the cart, 
this is so, if your game uses multiple carts, you can just write ```#include font/font.lua.p8l``` to have your custom font on all carts.
Enjoy!
