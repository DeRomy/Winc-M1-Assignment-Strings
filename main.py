# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)
report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute' 


# Part 2
player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name = player[player.find(' ')+1:] 

last_name_len = len(last_name)
name_short = f'{player[0]}. {last_name}'

chant = (len(first_name)-1) * (first_name + '! ') + (first_name + '!')
good_chant = chant[-1] != ' '