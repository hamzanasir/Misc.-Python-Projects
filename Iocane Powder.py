#> Man in Black: All right. Where is the poison? The battle of wits has begun.
#  It ends when you decide and we both drink, and find out who is right... and who is dead.

#The line above is from the perennial favorite 1980s movie adaptation of William Goldman's *The Princess Bride*, wherein a mysterious
# hero sits down to a battle of wits with a villainous Sicilian kidnapper. The setup: two cups positioned between the two, one of which
# (purportedly) contains a colorless, odorless, lethal poison (viz., iocane powder). After a guess is made as to which cup contains the
# poison, both drink, and the winner is the one left standing.

#The following program simulates multiple rounds of this battle of wits, allowing the player to repeatedly guess
#  which cup is poisoned. The computer will "place" the poison before the player guesses, and will reveal who is right... and who is dead, afterwards.

#At the outset, the computer will always place the poison in cup 2 before letting the player guess, but after enough guesses have been entered
#  the computer will start to place the poison based on the pattern of previous guesses so as to outsmart the player.

def record_guess(pattern_dict, pattern, guess):
    """Updates the `pattern_dict` dictionary by either creating a new entry
    or updating an existing entry for key `pattern`, increasing the count
    corresponding to `guess` in the list."""
    # YOUR CODE HERE
    if pattern not in pattern_dict:
        pattern_dict[pattern] = [0, 0]

    if int(guess) == 1:
        pattern_dict[pattern] = [pattern_dict[pattern][0] + 1, pattern_dict[pattern][1]]
    elif int(guess) == 2:
        pattern_dict[pattern] = [pattern_dict[pattern][0], pattern_dict[pattern][1] + 1]

def next_placement(pattern_dict, pattern):
    if pattern not in pattern_dict:
        return '2'
    elif pattern_dict[pattern][0]>pattern_dict[pattern][1]:
        return '2'
    elif pattern_dict[pattern][0]==pattern_dict[pattern][1]:
        return '2'
    else:
        return '1'

def play_interactive(pattern_length=4):
    poison='2'
    initialpat=''
    for _ in range(pattern_length):
        s=input('Where is the iocane powder? my cup(1) or yours(2)?')
        if s=='1' or s=='2':
            if s==poison:
                print('You were right! I be deadd.')
            else:
                print('Wrong!')
            initialpat+=s
        else:
            return
    patdic={}
    while True:
        s=input('Where is the iocane powder? my cup(1) or yours(2)?')
        if s=='1' or s=='2':
            poison=next_placement(patdic,initialpat)
            record_guess(patdic,initialpat,s)
            if s==poison:
                print('You were right! I be deadd.')
            else:
                print('Wrong!')
            newpat=initialpat[:0]+initialpat[1:]
            newpat+=s
            initialpat=newpat
        else:
            return

#main
play_interactive(10)