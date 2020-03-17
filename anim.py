from matplotlib.animation import FuncAnimation

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


# TODO:
#  draw circles to show Fourier coefficients
#  save animation so that it runs smoothly!
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c

class Animator(FuncAnimation):
	def __init__(self, fig, ax, fourier, T):
		# init function for FuncAnimation
		self.line, = ax.plot([], [], lw=3)
		self.x_data = []
		self.y_data = []

		def init():
			# create line and arrows
			self.x_data = []
			self.y_data = []
			self.line.set_data([], [])
			return self.line,


		# time delay between frames
		self.interval = 20
		total_frames = int(T*1000 // self.interval)
		kwargs = {
			"init_func": init,
			"frames": total_frames,
			"interval": self.interval,
			"blit": True
		}

		super().__init__(fig, self.animate, **kwargs)
		self.f = fourier


	def animate(self, i):
		t = i * (self.interval / 1000)

		p = self.f(t)[0]
		x, y = p.real, p.imag

		self.x_data.append(x)
		self.y_data.append(y)

		self.line.set_data(self.x_data, self.y_data)
		return self.line,


class Arrow:
	def __init__(self, ax, x, y, n, c):
		self.origin = x + 1j * y
		self.n = n
		self.c = c

		dx, dy = c.real, c.imag
		self.line = ax.arrow(x, y, dx, dy)

	def update(self, t):
		d = self.origin + self.c * np.exp(1j * self.n * t)
		points = [(i.real, i.imag) for i in (self.origin, self.origin + d)]
		self.line.set_xy(points)


if __name__ == "__main__":
	fig, ax = plt.subplots()
	ax.set_xlim([-2, 2])
	ax.set_ylim([-2, 2])
	a = Arrow(ax, 0, 0.2, 1, 1+1j)
	a.update(3.14)
	#anim = Animator(fig, ax, lambda x: [np.exp(1j * x)], 6.28)
	plt.show()