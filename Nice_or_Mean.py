

# Creating the Nice or Mean game in the Python Course for TTA
# 1 - 23 - 2024


def start(nice = 0, mean = 0, name = ''):
    # Get the users name 
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def describe_game(name):
    ''' Check if this game is new or not.
        if it is new, get the users name.
        If it is not new, thank the player for 
        playing and continue with the game
    '''
    # Meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    
    if name != '':
        print('\n>>> Thank you for playing again, {}'.format(name))
    
    else:
        stop = True
        while stop:
            if name == '':
                name = input('What is your name? \n>>> '.capitalize())
                if name != '':
                    print('\nWelcome, {}'.format(name))
                    print('\nIn this game, you will be greeted\nby several different people. \nYou can choose to be nice or mean')
                    print('but at the end of the game your fate \n will be sealed by your actions.')
                    stop = False
    return name 

def nice_mean(nice, mean, name):
    stop = True 
    while stop:
        show_score(nice, mean, name)
        pick = input('\nA stranger approaches you for a \nconversation. Will you be nice or mean? (N/M)\n>>> '.lower())
        if pick[0] == 'n':
            print('\nThe stranger walks away smiling...')
            nice += 1
            stop = False 
        if pick[0] == 'm':
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean += 1
            stop  = False
    score(nice, mean, name) # Pass the 3 variables to the score() 


def show_score(nice, mean, name):
    print('\n{}, your current total: \nNice: {}\nMean: {}'.format(name, nice, mean))

def score(nice, mean, name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # If the condition is valid, call Win function passing in the variables so it can use them
        win(nice, mean, name)
    if mean > 2: # If the condition is valid, call Win function passing in the variables so it can use them
        lose(nice, mean, name)
    else: 
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    print('\nNice job {}, you win! \nSo many people love you and you''ve \nmade so many friends along the way!'.format(name))
    # call again function and pass in our variables to play again
    again(nice, mean, name)


def lose(nice, mean, name):
    print('\nDarn {}, you lose! \nSo many people dislike you now. you live in a dirty beat-up \nvan by the river, wretched and alone!'.format(name))
    # call again function and pass in our variables to play again
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True 
    while stop:
        choice = input('\nDo you want to play again? (y/n): \n>>>'.lower())
        if choice[0] == 'y':
            stop = False
            reset(nice, mean, name)
        if choice[0] == 'n':
            stop = False
            quit() # We do not need to create a quit() function, in python it will automatically quit the program
        else: 
            print('\nEnter ( Y ) for ''YES'', ( N ) for ''NO'':\n>>>')

def reset(nice, mean, name):
    nice = 0
    mean = 0
    # We do not reset the name of the user because the same user has selected to play again
    start(nice, mean, name)


if __name__ == '__main__':
    start()