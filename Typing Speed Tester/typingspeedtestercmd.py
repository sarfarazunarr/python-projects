from time import *
import random as r



def mistakes(paratext, usertext):
    error = 0
    for i in range(len(paratext)):
        try:
            if paratext[i] != usertext[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(start, end, userinput):
    time_delay = end - start
    rounds = round(time_delay, 2)
    speed = len(userinput) / rounds

    return round(speed)



test = ['Life is like a bouncing ball you can easily calculate the law of physics with the help of formulas defined by scientst.', 'You can be a scientist in future', 'if you will study hard and write amazing research paper then you will be able to create amazing projects in science and can be a great scientist']

test1 = r.choice(test)
print()
print()
print('          ***** Typing Speed *****          ')
print(test1)
print()
print()
start_time = time()
testinput = input(' Start Typing...')
end_time = time()

print(' >>>> Speed: >>>>', speed_time(start_time, end_time, testinput), 'W/s')
print(' xxxx Error: xxxx', mistakes(test1, testinput))


# It will give you the index of letter that you have typed wrong.
# If you wants GUI sample then you can go back and see other file in this folder.
