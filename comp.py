with open('f_name.py', 'w') as py, open("f_name.p70", 'r') as p70:
    py.write(p70.read())
    py.write('''
    ''')
    py.write("""
with open('f_name.py', 'w') as py, open("f_name.p70", 'r') as p70:
    def mas_rm(masive, num, num1, num2, num3, num4, num5, num6):
        global massiveee
        massive = masive[num]
        massivee = massive[num1:num2]
        massiveee = str(massivee)

        global simvolll
        simvol = masive[num]
        simvoll = simvol[num3:num4]
        simvolll = str(simvoll)

        global perr
        per = masive[num]
        perr = per[num5:num6]

        
    for i in range(0, ix):
        mas_rm(program, i, 0, 5, 6, len(program[i]), None, None)
        if massiveee ==  'write':        
            py.write('print' + simvolll) 
            py.write('''
''')   

        mas_rm(program, i, 0, 4, 5, len(program[i]), None, None)
        if massiveee == 'pass':
            py.write('input' + simvolll)
            py.write('''
''')
        mas_rm(program, i, 0, 3, 3, 6, 6,len(program[i]))
        if massiveee == 'for':
            py.write(massiveee + simvolll + "in range" + perr)

        mas_rm(program, i, 0, 3, 4, len(program[i]), None, None)
        if massiveee == 'var':
            py.write(simvolll)
            py.write('''
''')
        """)

import os
os.system('python f_name.py')
os.system('python f_name.py ')#&& rm f_name.py')
    