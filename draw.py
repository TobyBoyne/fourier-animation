"""
Allows the user to draw onto a pyplot axis

Uses matplotlib.pyplot events:
 - button_press_event
 - button_release_event
 - motion_notify_event
"""

import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

class Drawer:
	def __init__(self, fig, ax):
		self.fig = fig
		self.ax = ax

		# points is stored as a 2D array with 3 columns - time, x coord, y coord
		self.points = np.array([])
		self.record_data = False
		self.start_time = 0

		click_id =	fig.canvas.mpl_connect('button_press_event', self.draw_line)
		move_id =	fig.canvas.mpl_connect('motion_notify_event', self.plot_point)

	def draw_line(self, event):
		"""Start recording data"""
		self.record_data = True
		self.start_time = perf_counter()

	def plot_point(self, event):
		if self.record_data and event.inaxes:
			ax.plot(event.xdata, event.ydata, marker="x")
			plt.draw()

if __name__ == "__main__":
	fig, ax = plt.subplots()
	ax.plot([1,2,3,4,5])
	draw = Drawer(fig, ax)

	plt.show()