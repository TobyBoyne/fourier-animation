import matplotlib.pyplot as plt
import numpy as np

from draw import Drawer
from fourier import Fourier

def split_points(points):
	xs = points[:, :2]
	ys = points[:, (0,2)]

	return xs, ys

if __name__ == "__main__":
	fig, ax = plt.subplots()
	ax.set_xlim([0, 1])
	ax.set_ylim([0, 1])
	draw = Drawer(fig, ax)
	plt.show()

	xs, ys = split_points(draw.points)

	fourier_x = Fourier(xs, 5)
	fourier_y = Fourier(ys, 5)

	ts = xs[:, 0]
	plt.plot(ts, [fourier_x(t) for t in ts])
	plt.show()