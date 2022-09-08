import os
os.system("clear")

#name = input("Name ---> ")

name = 'f_name.p70'
#print("syntax = ['write, pass, var, #Exit'], Start program --> 1: num")

pos = open(name, 'w')
pos.write('program = [')

#f.write("'"+query+"',\n")

while True:
    #with open("f_name.pos", 'a') as pos:
    i = input(": ")
    pos.write('"'+i +'",\n')
    if i == "#exit":
        break
pos.write("]")
ix = input("0: ")
pos.write('\n')
pos.write('ix = ' + ix)
#os.system("cat f_name.p70")