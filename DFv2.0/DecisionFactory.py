import random
#import numpy as np

'''
Thurs, Feb 7 2019: ~8:15 pm
    Matt - added underscores in names of some variables and functions, and to "__init__"
           to make it work with our framework. Those function and variable names
           are the ones used in the book, but if that was done on purpose I can just
           as easily change the ones in the framework to match the ones
           Sean had
'''

class DecisionFactory:
	def __init__(self, name='Walter Wanderley'):
		self.name = name
		self.directions = ['wait', 'up', 'down', 'right', 'left']
		self.failed_directions = []
		self.last_result = 'start'
		self.last_direction = 'wait'

	#Note: we have relativistic coordinates recorded here, since the map
	# is relative to the player's sfirst known and recorded position:
	#self.state.pos = (0,0)

	def get_decision(self, verbose = True):
		# return self.random_direction()
		return self.better_than_random()

	def random_direction(self):
		#random.randint(0,4) #Includes wait state
		r = random.randint(1,4) #Does NOT include wait state

		return self.directions[r]

	def better_than_random(self):
		r = self.random_direction()

		# print "Last result: ", self.last_result
		# print "Last direction: ", self.last_direction

		self.failed_directions.extend(self.last_direction)

		if self.last_result != 'success':
			self.failed_directions.extend(self.last_direction)

			r = random.randint(1,4)

			while self.directions[r] in self.failed_directions:
				# print "Failed:", self.failed_directions
				r = random.randint(1,4)

			# print self.directions[r]
			return self.directions[r]
		
		else:	
			self.failed_directions = []


			# r = self.last_direction
			r = self.random_direction()
			# print r
			return r

	def put_result(self, result):
		self.result = result