from matplotlib.animation import FuncAnimation

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')




def init():
	line.set_data([], [])
	return line,
def animate(i):
	x = np.linspace(0, 4, 1000)
	y = np.sin(2 * np.pi * (x - 0.01 * i))
	line.set_data(x, y)
	return line,



class Animator(FuncAnimation):
	def __init__(self, fig, T):
		fps = 20
		kwargs = {
			"init_func": init,
			"frames": T // fps,
			"interval": fps,
			"blit": True
		}
		super().__init__(fig, self.animate, **kwargs)

	def animate(self, i):
		pass

# anim = FuncAnimation(fig, animate, init_func=init,
# 							   frames=100, interval=20, blit=True)


if __name__ == "__main__":
	fig = plt.figure()
	ax = plt.axes(xlim=(0, 1), ylim=(0, 1))
	line, = ax.plot([], [], lw=3)
	anim = Animator(fig, 1000)