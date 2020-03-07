import matplotlib.pyplot as plt
import numpy as np

from draw import Drawer
from fourier import Fourier
from anim import Animator

def split_points(points):
	"""Split the [t, x, y] points into [t, x] and [t, y] so that two different Fourier series can be made"""
	xs = points[:, :2]
	ys = points[:, (0,2)]

	return xs, ys

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
	xs, ys = split_points(draw.points)

	fourier_x = Fourier(xs, N)
	fourier_y = Fourier(ys, N)

	# --- plot drawn shape against Fourier approximation ---
	ts = np.linspace(xs[0, 0], xs[-1, 0], 100)
	plt.plot(fourier_x(ts), fourier_y(ts))
	plt.plot(xs[:, 1], ys[:, 1])
	plt.show()

	# --- animate Fourier drawing ---
	anim_fig, anim_ax = plt.subplots()
	anim = Animator(anim_fig, anim_ax, fourier_x, fourier_y, ts[-1])
	plt.show()