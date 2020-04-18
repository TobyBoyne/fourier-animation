import matplotlib.pyplot as plt
import numpy as np

from draw import Drawer
from fourier import Fourier
from anim import Animator, GroupAnimator


def run(Ns, save_anim=False):
	# --- user input ---
	fig, ax = plt.subplots()
	ax.set_xlim([0, 1])
	ax.set_ylim([0, 1])
	draw = Drawer(fig, ax)
	plt.show()

	# --- find Fourier series for drawn shape ---
	fouriers = [Fourier(draw.points, N) for N in Ns]

	# --- plot drawn shape against Fourier approximation ---
	fig, axs = plt.subplots(1, len(Ns))
	ps = draw.points
	t_start, t_end = ps[0, 0].real, ps[-1, 0].real
	ts = np.linspace(t_start, t_end, 100)

	fs = [f(ts) for f in fouriers]
	for ax, f in zip(axs, fs):
		ax.plot(ps[:, 1].real, ps[:, 1].imag)
		ax.plot(f.real, f.imag)

	plt.legend(("User Input", "Fourier Approximation"))
	plt.show()

	# --- animate Fourier drawing ---
	anim_fig, anim_axs = plt.subplots(1, len(Ns))
	anim_fig.suptitle(f"Fourier approximations of orders {Ns}")
	anims = []
	for anim_ax, fourier in zip(anim_axs, fouriers):
		anim_ax.set_xlim([0, 1])
		anim_ax.set_ylim([0, 1])
		anim_ax.set_title(f"N = {len(fourier.n) // 2}")
		anims.append(Animator(anim_ax, fourier))

	group_anim = GroupAnimator(anim_fig, anims, ts[-1])

	if save_anim:
		fig.savefig('images\comparison.png')
		group_anim.save('images\drawing.gif', writer='imagemagick', fps=30)
	plt.show()

if __name__ == "__main__":
	# number of coefficients in Fourier series
	Ns = (2, 12)

	run(Ns, save_anim=True)