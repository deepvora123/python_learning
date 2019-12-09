# Instead of making a tuple with xyz = (srg,gerge,gergerg,)
# Make a list with []


game= [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]



# game[0][1]=1 can be used to modify

def print_game(player=0, row=0, coloumn=0):
	print("   a  b  c")
	game[row][coloumn] = player
	for count, row in enumerate(game):
		print(count, row)

print_game(1,2,0)
print_game(2,1,2)

'''
def change(x,y):
	game[x][y]=1

x = input('enter x and y cordinates to change')
change(2,1)

game[0][1]=1
print_game()
'''







