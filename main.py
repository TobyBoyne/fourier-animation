import matplotlib.pyplot as plt
import numpy as np

from draw import Drawer
from fourier import Fourier
from anim import Animator


if __name__ == "__main__":
	# number of coefficients in Fourier series
	N = 10

	# --- user input ---
	fig, ax = plt.subplots()
	ax.set_xlim([0, 1])
	ax.set_ylim([0, 1])
	draw = Drawer(fig, ax)
	plt.show()

	# --- find Fourier series for drawn shape ---
	fourier = Fourier(draw.points, N)

	# --- plot drawn shape against Fourier approximation ---
	ps = draw.points
	t_start, t_end = ps[0, 0].real, ps[-1, 0].real
	ts = np.linspace(t_start, t_end, 100)
	plt.plot(ps[:, 1].real, ps[:, 1].imag)

	f = fourier(ts)
	plt.plot(f.real, f.imag)

	plt.legend(("User Input", "Fourier Approximation"))
	plt.show()

	# --- animate Fourier drawing ---
	anim_fig, anim_ax = plt.subplots()
	anim = Animator(anim_fig, anim_ax, fourier, ts[-1])
	anim.save('gifs\drawing.gif', writer='imagemagick', fps=30)
	plt.show()