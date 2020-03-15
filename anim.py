from matplotlib.animation import FuncAnimation

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


# TODO:
#  draw circles to show Fourier coefficients
#  save animation so that it runs smoothly!
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c

class Animator(FuncAnimation):
	def __init__(self, fig, ax, fourier_x, fourier_y, T):
		# init function for FuncAnimation
		self.line, = ax.plot([], [], lw=3)
		self.x_data = []
		self.y_data = []

		def init():
			self.x_data = []
			self.y_data = []
			self.line.set_data([], [])
			return self.line,


		# time delay between frames
		self.interval = 20
		self.total_frames = int(T*1000 // self.interval)
		kwargs = {
			"init_func": init,
			"frames": self.total_frames,
			"interval": self.interval,
			"blit": True
		}

		super().__init__(fig, self.animate, **kwargs)
		self.T = T
		self.f_x = fourier_x
		self.f_y = fourier_y


	def animate(self, i):
		print(self.total_frames, i)
		t = i * (self.interval / 1000)

		x = self.f_x(t)[0]
		y = self.f_y(t)[0]

		self.x_data.append(x)
		self.y_data.append(y)

		self.line.set_data(self.x_data, self.y_data)
		return self.line,


if __name__ == "__main__":
	fig, ax = plt.subplots()
	anim = Animator(fig, ax, np.sin, np.cos, 6.28)
	plt.show()