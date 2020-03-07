from matplotlib.animation import FuncAnimation

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


def init():
	line.set_data([], [])
	return line,


class Animator(FuncAnimation):
	def __init__(self, fig, fourier_x, fourier_y, T):
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
		line.set_data(xs, ys)
		return line,


if __name__ == "__main__":
	fig = plt.figure()
	ax = plt.axes(xlim=(-1, 2), ylim=(-1, 2))
	line, = ax.plot([], [], lw=3)
	anim = Animator(fig, np.sin, np.cos, 6.28)
	plt.show()