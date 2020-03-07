from matplotlib.animation import FuncAnimation

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

class Animator(FuncAnimation):
	def __init__(self, fig, ax, fourier_x, fourier_y, T):

		# init function for FuncAnimation
		self.line, = ax.plot([], [], lw=3)
		def init():
			self.line.set_data([], [])
			return self.line,



		fps = 20
		self.total_frames = int(T*1000 // fps)
		kwargs = {
			"init_func": init,
			"frames": self.total_frames,
			"interval": fps,
			"blit": True
		}

		super().__init__(fig, self.animate, **kwargs)
		self.T = T
		self.f_x = fourier_x
		self.f_y = fourier_y


	def animate(self, i):
		ts = np.linspace(0, self.T * i/self.total_frames, 50)

		xs = self.f_x(ts)
		ys = self.f_y(ts)
		self.line.set_data(xs, ys)
		return self.line,


if __name__ == "__main__":
	fig, ax = plt.subplots()
	anim = Animator(fig, ax, np.sin, np.cos, 6.28)
	plt.show()