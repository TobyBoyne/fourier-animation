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
		self.arrows = create_arrows(ax, fourier)
		self.x_data = []
		self.y_data = []

		def init():
			# create line and arrows
			self.x_data = []
			self.y_data = []
			self.line.set_data([], [])
			return (self.line, *[a.line for a in self.arrows])


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
		
		last_end = 0 + 0j
		for arrow in self.arrows:
			# update each arrow, starting the arrow at the end of the previous one
			last_end = arrow.update(last_end, t)

		return (self.line, *[a.line for a in self.arrows])


class Arrow:
	def __init__(self, ax, x, y, n, c, L):
		self.n = n
		self.c = c
		self.L = L

		dx, dy = c.real, c.imag
		self.line, = ax.plot((x, x + dx), (y, y + dy), lw=1)

	def update(self, start, t):
		end = start + self.c * np.exp(-1j * self.n * t * 2 * np.pi / self.L)
		points = [
			(start.real, end.real),
			(start.imag, end.imag)
		]
		self.line.set_data(points)

		return end


def create_arrows(ax, fourier):
	"""Create arrows from the coefficients of a Fourier series"""
	p = 0 + 0j
	arrows = []
	for c, n in zip(fourier.c, fourier.n):
		arrow = Arrow(ax, p.real, p.imag, n, c, fourier.L)
		arrows.append(arrow)
		p += c

	return arrows


if __name__ == "__main__":
	fig, ax = plt.subplots()
	ax.set_xlim([-2, 2])
	ax.set_ylim([-2, 2])
	#a = Arrow(ax, 0, 0.2, 1, 1+1j)
	#anim = Animator(fig, ax, lambda x: [np.exp(1j * x)], 6.28)
	plt.show()