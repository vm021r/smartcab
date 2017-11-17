import numpy as np
import random
valid_actions = [None, 'forward', 'left', 'right']

# dic = {'a':{'a':1,
#             'b':2},
#        'b':{'c':3,
#             'd':4},
#        'c':{'e':5,
#             'f':6},
#        'd':{'g':7,
#             'h':8}
#       }

dic = {}
def f():

    if not (state in dic.keys()):
        dic[state] = {action: 0.0 for action in valid_actions}
    else:
        # if not (action in dic[state].keys()):
        #     dic[state][action] = Q2
        #else:
        dic[state][action] = Q3

    return dic

state = 'a'
#action = 'a'
# Q1 = 888
# Q2 = 999
Q3 = 777

print state
print f()

#state = 'a'
#action = 'z'

# print state
# print f()

state = 'e'
#action = 't'

print state
print f()

action = valid_actions[2]

print state
print f()