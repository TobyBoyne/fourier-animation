import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from fourier import Fourier

# time delay between frames
INTERVAL = 20

class GroupAnimator(FuncAnimation):
	def __init__(self, anims, T):
		self.anims = anims
		total_frames = int(T * 1000 // INTERVAL)
		kwargs = {
			"init_func": self.init_func,
			"frames": total_frames,
			"interval": INTERVAL,
			"blit": True
		}

		super().__init__(fig, self.animate, **kwargs)

	def init_func(self):
		anim_data = []
		for anim in self.anims:
			anim_data += anim.init_func()
		return anim_data

	def animate(self, i):
		anim_data = []
		for anim in self.anims:
			anim_data += anim.animate(i)
		return anim_data


class Animator:
	"""Object stores all lines to be animated
	Main drawing stored in self.line
	Arrows of coefficients stored in self.arrows
	init() is called at the beginning of each loop
	animate() is called at each frame"""
	def __init__(self, fig, ax, fourier, T):
		# init function for FuncAnimation
		self.line, = ax.plot([], [], lw=3)
		self.arrows = create_arrows(ax, fourier)
		self.x_data = []
		self.y_data = []

		# def init():
		# 	# create line and arrows
		# 	self.x_data = []
		# 	self.y_data = []
		# 	self.line.set_data([], [])
		# 	return (self.line, *[a.line for a in self.arrows])


		# time delay between frames
		# self.interval = 20
		# total_frames = int(T*1000 // self.interval)
		# kwargs = {
		# 	"init_func": self.init_func,
		# 	"frames": total_frames,
		# 	"interval": self.interval,
		# 	"blit": True
		# }
		#
		# super().__init__(fig, self.animate, **kwargs)
		self.f = fourier

	def init_func(self):
		self.x_data = []
		self.y_data = []
		self.line.set_data([], [])
		return [self.line, *[a.line for a in self.arrows]]

	def animate(self, i):
		t = i * (INTERVAL / 1000)

		p = self.f(t)[0]
		x, y = p.real, p.imag

		self.x_data.append(x)
		self.y_data.append(y)
		self.line.set_data(self.x_data, self.y_data)

		last_end = 0 + 0j
		for arrow in self.arrows:
			# update each arrow, starting the arrow at the end of the previous one
			last_end = arrow.update(last_end, t)

		return [self.line, *[a.line for a in self.arrows]]


class Arrow:
	"""Straight line that represents a coefficient of the Fourier series"""
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
	fig, axes = plt.subplots(1, 2)
	fig.set_size_inches(18.5, 10.5)

	ts = np.linspace(0, 6.28, 100)
	xs = 0.5 * np.cos(ts) + 0.5 * np.cos(2 * ts)
	ys = np.sin(ts) + 0.25

	points = np.array([ts, xs + 1j * ys]).T

	anims = []
	for n, ax in enumerate(axes):
		f = Fourier(points, N=n+1)
		anims.append(Animator(fig, ax, f, 6.28))
		ax.set_xlim((-2, 2))
		ax.set_ylim((-2, 2))
	group_anims = GroupAnimator(anims, 6.28)
	plt.show()