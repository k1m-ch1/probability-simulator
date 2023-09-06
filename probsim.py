import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

class ProbabilitySimulator:

	_collector = {1:0}

	def __init__(self, p, frames):
		"""
			p is the probability of success
		"""
		if type(frames) == int and frames > 0:
			self._frames = frames 
		else:
			raise ValueError("frames must be a positive integer")

		if 0 < p < 1:
			self._p = p
		else:
			raise ValueError("Probability of success must be in between 0 and 1")

	@property
	def frames(self):
		return self._frames
	
	@property
	def p(self):
		return self._p

	@p.setter
	def p(self, value):
		self._p = value

	@property
	def collector(self):
		return self._collector
	
	@collector.setter
	def collector(self, value):
		if type(value) == dict:
			self._collector = value
		else:
			raise ValueError('collector must be a dictionary')

	def place_text(self, ax, text, fontsize=8, color='red'):
		ax.text(-0.1, -0.12, text, fontsize=fontsize, color=color, transform=ax.transAxes)


	def run_probability(self, n):
		return np.random.rand(n) < self.p

	def play_animation(self, animation_function, max_frames=None, fps=30, title='My Graph', x_label='X-axis', y_label='Y-axis'):
		"""
			This function adds data to the graph every frame.
			animation_function is the animate function that plays every frame. 
		"""
		fig, ax = plt.subplots(figsize=(8, 4.5))
		plt.xticks(rotation=90)
		def animate(frame):
			ax.clear()
			result = animation_function(frame=frame, fig=fig, ax=ax)
			ax.set_title(title, fontsize=7)
			plt.xticks(rotation=45)
			ax.set_xlabel(x_label)
			ax.set_ylabel(y_label)
			plt.xticks(np.arange(1, t:=max(self.collector.keys()), t//10 + 1))

			return result

		anim = FuncAnimation(fig, animate, frames=max_frames if max_frames is not None else self.frames, repeat=False, interval=(1/fps)*1000)
		plt.show()


class GeometricDistribution(ProbabilitySimulator):

	def __init__(self, p, number_of_success):
		super().__init__(p, number_of_success)

	def run_probability(self):
		n = int(1//self.p)		
		i = 0
		while len(possibilities:=np.where(super().run_probability(n))[0]) == 0:
			i += n
		i += possibilities[0] + 1
		return i


	def play_adding_value_animation(self):
		self.collector = dict()
		def animation_function(frame, fig, ax):
			self.place_text(ax, f"Frame: {frame}")

			index_of_success = self.run_probability()
			self.collector[index_of_success] = self.collector.get(index_of_success, 0) + 1
			new_bars = ax.bar(self.collector.keys(), self.collector.values())
			return new_bars

		super().play_animation(animation_function, title=f"Geometric distribution\nMax Frame:{self.frames}", x_label='Index Of Success', y_label='Count')

	def get_probability_bars(self, fig, ax):
		self.collector = dict() 
		for _ in range(1, self.frames+1):
			res = self.run_probability()
			self.collector[res] = self.collector.get(res, 0) + 1
		return ax.bar(self.collector.keys(), self.collector.values())

	def play_changing_probability_animation(self):
		p_prev = self.p
		def animate_function(frame, fig, ax):
			self.p = (frame+1)/100
			result = self.get_probability_bars(fig=fig, ax=ax)
			self.place_text(ax, f'Probability: {frame/100}\nFrame: {frame}')
		super().play_animation(animate_function, max_frames=100, fps=30, title=f"Geometric distribution\nMax Frame: {100}", x_label='Index Of Success', y_label='Count')
		self.p = p_prev

class BinomialDistribution(ProbabilitySimulator):

	def reset_collector(self):
		self.collector = {x:0 for x in range(self.n+1)}

	def __init__(self, n, p, frames):
		self._n = n
		self.reset_collector()
		super().__init__(p, frames)

	@property
	def n(self):
		return self._n

	def run_probability(self):
		return super().run_probability(self.n)

	def play_adding_value_animation(self):
		self.reset_collector()

		def animation_function(frame, fig, ax):
			self.collector[self.run_probability().sum()] += 1
			self.place_text(ax, f"Frame: {frame}")
			return ax.bar(self.collector.keys(), self.collector.values())
		
		super().play_animation(animation_function, title=f"Binomial distribution\nMax Frames: {self.frames}", x_label='Index Of Success', y_label='Count')


	def play_changing_probability_animation(self):

		def animation_function(frame, fig, ax):
			self.reset_collector()
			p_prev = self.p
			self.p = (frame + 1)/100
			self.place_text(ax, f"Frame: {frame}\nProbability: {self.p}")
			for _ in range(self.frames):
				self.collector[self.run_probability().sum()] += 1
			
			result = ax.bar(self.collector.keys(), self.collector.values())
			self.p = p_prev
			return result

		super().play_animation(animation_function, max_frames=100, title=f"Binomial distribution\nMax Frames: {100}", x_label='Index Of Success', y_label='Count')




if __name__ == '__main__':
	X = BinomialDistribution(15, 0.5, 10_000)
	X.play_changing_probability_animation()

	# X = GeometricDistribution(0.3, 1000)
	# X.play_adding_value_animation()
