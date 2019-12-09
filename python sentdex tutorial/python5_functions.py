
game= [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]



def print_game(player=0, row=0, coloumn=0, just_display=False):
	print("   a  b  c")
	if player !=0:
		game[row][coloumn] = player
	for count, row in enumerate(game):
		print(count, row)

print_game(just_display=True)
print_game(2,1,2)


def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")