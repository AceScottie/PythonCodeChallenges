"""
A New bus company has developed an app that allows users to pay for their ticket prior to getting on the bus and simply scan their ticket on the bus.
The users bus stop has been associated with their ticket.
To prevent the usual shuffeling whith people getting on and off the bus, users are to be designated a seat when they get on.

Your task is to create a solution that allows all people to get off the bus without pushing past other people!
A user in the isle seat can get off at their stop without restriction.
A user in a window seat will only get off when the isle seat next to them is free.
A user who misses the stop will stay on the bus to the last stop to complain!

Additionally:
You may program in a function that allerts a user in an isle seat to move to any open window seat as long as both the window and isle seats are empty.
"""


import random
class bus_travel:
	def __init__(self, stops):
		self.fails = 0
		self.bus = [
		[[None, None], [None, None]], #4
		[[None, None], [None, None]], #8
		[[None, None], [None, None]], #12
		[[None, None], [None, None]], #16
		[[None, None], [None, None]], #20
		[[None, None], [None, None]], #24
		[[None, None], [None, None]], #28
		[[None, None], [None, None]], #32
		[[None, None], [None, None]], #36
		[[None, None], [None, None]], #40
		[[None, None], [None, None]], #44
		[[None, None], [None, None]], #48
		[[None, None], [None, None]], #52
		[[None, None], [None, None]], #56
		[[None, None], [None, None]], #60
		[[None, None], [None, None]], #64
		[[None, None], [None, None]], #68
		[[None, None], [None, None]], #72
		[[None, None], [None, None]], #76
		[[None, None], [None, None]], #80
		]
		self.current_stop = 0
		self.max_stops = stops
		self.people_on = 0
		self.people_off = 0
	def _get_off(self):
		for seats in self.bus:
			if seats[0][1] == self.current_stop or seats[0][1] is None:
				if seats[0][1] is not None:	self.people_off+=1
				seats[0][1] = None
				if seats[0][0] == self.current_stop  or seats[0][0] is None:
					if seats[0][0] is not None:	self.people_off+=1
					seats[0][0] = None
			if seats[1][0] == self.current_stop  or seats[1][0] is None:
				if seats[1][0] is not None:	self.people_off+=1
				seats[1][0] = None
				if seats[1][1] == self.current_stop  or seats[1][1] is None:
					if seats[1][1] is not None:	self.people_off+=1
					seats[0][0] = None
	def _stop(self) -> list:
		self.current_stop += 1
		if self.current_stop == self.max_stops:
			return []
		people = []
		for i in range(random.randint(1, 5)):
			people.append(random.randint(self.current_stop+1, self.max_stops))
		self.people_on+=len(people)
		if self.people_on-self.people_off > 80:
			raise Exception(f"Too many people on the bus {self.people_on-self.people_off}/80, You failed")
		return people
	def _scan(self):
		for row in self.bus:
			for seats in row:
				for seat in seats:
					if seat is not None and seat >= self.current_stop:
						print("A Person failed to get off the bus")
						self.fails += 1
	##user access functions
	def row(self, x:int):
		"""
		reuturns the selected row (x) of the bus as [[window_seat, isle_seat],[isle_seat, window_seat]]
		"""
		return self.bus[x]
	def seat(self, x:int) -> tuple:
		"""
		returns the row index and X Y position of the seat number
		"""
		seats = [[0,0], [0,1], [1,0], [1,1]]
		s = x%4
		r = (x-s)/4
		if r <= 1: r = 1
		return r-1, seats[s] # row index, seat L/R, L/R
	def set(self, row:int, seat:list, person:int):
		"""
		input the row and seat position to make the inputted person sit there
		"""
		if self.bus[row][seat[0]][seat[1]] is None:
			self.bus[row][seat[0]][seat[1]] = person
		else:
			raise Exception("There is already a person sat there.")


##Add your code to the solution method.
def solution(bus:bus_travel, people:list):
	"""
	example code:
	for s, person in enumerate(people): ## for the next person in the list of people set s to the increment
		row, seat = bus.seat(s) ## get the row and x,y values of the seat index
		if bus.row(row)[seat[0]][seat[1]] is None: ## if the selected seat is empty
			bus.set(row, seat, person) ## tell the person to sit in that seat
	"""
	

if __name__ == "__main__":
	bus = bus_travel(100)
	while bus.current_stop < bus.max_stops:
		people = bus._stop()
		solution(bus, people)
		bus._get_off()
		bus._scan()
	print(f"{bus.fails} people failed to get off at the correct stop")
	print(f"{bus.people_on} people got on your bus and {bus.people_off} got off")
	
