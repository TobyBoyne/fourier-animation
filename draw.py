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
		# initialise to None - is set to a value when points are plotted
		self.points = None
		self.record_data = False
		self.start_time = 0

		click_id =	fig.canvas.mpl_connect('button_press_event', self.start_plotting)
		move_id =	fig.canvas.mpl_connect('motion_notify_event', self.plot_point)
		stop_id =	fig.canvas.mpl_connect('button_release_event', self.stop_plotting)

	def start_plotting(self, event):
		"""Start recording data"""
		self.record_data = True
		self.start_time = perf_counter()

	def plot_point(self, event):
		"""Plot a point at the current mouse (x, y) position
		Record the time at which this point was plotted
		If the mouse has not yet been clicked, or the cursor is outside of axes, don't plot a point"""
		if self.record_data and event.inaxes:
			x, y = event.xdata, event.ydata
			ax.plot(x, y, marker="x")
			plt.draw()

			t = perf_counter() - self.start_time
			if self.points is not None:
				self.points = np.append(self.points, [[t, x, y]], axis=0)
			else:
				self.points = np.array([[t, x, y]])

	def stop_plotting(self, event):
		"""Stop recording data"""
		self.record_data = False

if __name__ == "__main__":
	fig, ax = plt.subplots()
	ax.plot([1,2,3,4,5])
	draw = Drawer(fig, ax)
	plt.show()
	print(draw.points, draw.points.shape)