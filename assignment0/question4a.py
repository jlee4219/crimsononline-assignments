import random
# number of rounds and players
rounds = 5
players = 3

# simulates one game of look away
def lookaway_game():
    # keep track of who's still playing
    still_in = [True] * players

    # let forward = 0.  The other options are assigned 1 - 4
    for i in range(rounds):
        for j in range(players):

            # if one of them looks forward, they're no longer in
            if (random.randint(0,4) == 0):
                still_in[j] = False

    # if any are still in, Luigi loses. Represent with 0
    if(reduce(lambda x, y: x or y, still_in, False)):
        return 0

    # Otherwise Luigi wins.  Represent with 1
    else:
        return 1

def lookaway (n):
    # check the input, make sure it makes sense
    if n > 0:
        wins = 0
        for i in range(n):
            wins += lookaway_game()
        print "Luigi won " + str((float)(wins) / (float)(n)) + " of the games."
    else:
        print "Please give a positive number of trials."

