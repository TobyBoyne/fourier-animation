"""
Allows the user to draw onto a pyplot axis

Uses matplotlib.pyplot events:
 - button_press_event
 - button_release_event
 - motion_notify_event
"""

import matplotlib.pyplot as plt

class Drawer:
	def __init__(self, fig):
		self.fig = fig

