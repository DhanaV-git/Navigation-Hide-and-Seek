Part 1 : Report


Successor function takes a single state and gives a set of states that it could enter next in one move
Here the successor function of P in map.txt updates as follows: ( with index starting as 1 in theory)
Succ(P): (5,0) -> (4,0)
Succ(P): (4,0) -> (3,0)
Succ(P): (3,0) -> (2,0)
Succ(P): (2,0) -> { (2,1) , (1,0)}
		  Succ((2,1)) : (2,1) -> (2,2); Succ(2,2) : (2,2) -> {(2,3),(3,2)}; 
									Succ(2,3) -> False
									Backtrack to (2,2)
									Succ(2,2) -> (3,2)
										     Succ(3,2)->(4,2) ; Succ(4,2) ->(5,2); Succ(5,2)->(6,2)

This will go on till the path at a certain depth has been traced until it has met with an obstacle and record the path in move_str
If the certain path has been met with an obstacle, the record till the backtracking will be popped as the first element and the trace continues

In record, the loop runs infinitely as the nodes has not been marked as visited. So the successor function takes the visited nodes also as a possible nodes which
makes the loop run infinitely.
So, I have considered marking the visited nodes as reached and mark them along with the path needed to reach and this makes the successor function choose the not
visited nodes to be added to reached.

This will define the path to be traversed to reach the destination node in the shortest cost.



Part 2 : Report

Initial state would be k=1 since the assumption here is k>=1; if we consider the least, it has to be atleast k=1
goal state : if the number of p's in the end_board or the new_board matches with the given number of k
Successor function:
My idealogy of implementing this will be :
	-> Consider the start point as (0,0) and trace for the existing p's in the row and column. if there is any p's in row/column, check if those were seperated 
		by 'X' or '@' and not by '.'
	-> if the condition satisfies, then place the p in the starting position. Please note that the second method can be with the start point as the location of p
		However, the drawback here is, if there are more than one p's in the initial_board, the start point to be taken may become a slight complex, because the
		outcome of the final board may change with the consideration
	-> if the condition is not satisfied, check for the position of p in the row,column and move accordingly. i.e., if the existing p is row move to next row or check 
		for any X in that row and go to the places after X marked with '.' but not with '@'. Check the same possibility of step1 by updating the index, and repeat
		this step for columns if required or for both if needed.
	-> update the position of newly placed p and the existing p in to the array/list stating occupied, so that we don't need to compare all the positions unnecessarily
		Here, there can be another solution, we can even upadte the positions of 'X' and '@' as occupied. and mark the '.' as unoccupied. 
	-> By varying with indexes of both the lists, there might be a chance we can predict the unoccupied as well as the positions of occupied p's and check for alternatives
		simulataneously
	-> However, marking each node as occupied for p determines only for the existing nodes and not for the to be occupied nodes. For example, if I want to place a
		p in the place of '.' and the position of the existing p has been marked in that row or column I might look for the other oppurtunities in placing the new p
		instead searching for the X or @ in between 2 P's since X and @ has been marked as occupied. Determing the meaning of each symbol may become complex.
	I am searching for the alternatives for the time being...
