# fourier-animation
Recreates a hand-drawn image by calculating its complex Fourier Series representation.

## Usage
Run the `main.py` file, and draw the image in the figure that opens. Once the image has been drawn, close the figure. The next figure shows a comparison between the Fourier approximations, and the hand drawn image. Close this figure to create the drawing animation.
To change the number of coefficients of the Fourier series produced, change the values in the `Ns` tuple. To add/substract the number of Fourier series produced, add/remove values to/from the `Ns` tuple. To not save the figure (this will make the project run faster), pass `save_anim=False` into the `run()` function.

## Author
Created by Toby Boyne
Inspired by 3Blue1Brown's video: [But what is a Fourier series?](https://youtu.be/r6sGWTCMz2k)
