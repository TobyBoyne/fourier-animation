"""
Allows the user to draw onto a pyplot axis

Uses matplotlib.pyplot events:
 - button_press_event
 - button_release_event
 - motion_notify_event
"""

import matplotlib.pyplot as plt
import numpy as np

class Drawer:
	def __init__(self, fig):
		self.fig = fig
		self.points = np.array([])
		self.record_data = False

	def draw_line(self, event):
		print(event.xdata)
		

fig, ax = plt.subplots()
ax.plot([1,2,3,4,5])
draw = Drawer(fig)
user_input = fig.canvas.mpl_connect('button_press_event', draw.draw_line)
plt.show()
# while True:
# 	draw.draw_line() # here you click on the plot