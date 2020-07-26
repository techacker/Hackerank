# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets + 1 point for each occurrence of the substring in the string S.

# For Example:
# String = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Task
# Your task is to determine the winner of the game and their score.

S = input().upper()

def minion_game(string):
    KScore = 0
    SScore = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            KScore += len(string) - i
        else:
            SScore += len(string) - i

    # Calculate Scores and declare winner
    if SScore > KScore:
        print('Stuart', SScore)
    elif KScore > SScore:
        print('Kevin', KScore)
    else:
        print('Draw')

minion_game(S)
