import sys

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4
ADD = 5

# Variables
memory = [0] * 256
register = [0] * 8
pc = 0  # Program Counter, index of the current instruction
running = True

filename = sys.argv[1]

with open(filename) as f:
    for address, line in enumerate(f):
        line = line.split('#')
        try:
            v = int(line[0])
        except ValueError:
            continue

        memory[address] = v

print(memory[:15])

sys.exit(0)

while running:
	ir = memory[pc]  # Instruction register
	# if ir == PRINT_BEEJ:
	# 	print("Beej!")
	# 	pc += 1
	# elif ir == SAVE_REG:
	# 	reg_num = memory[pc + 1]
	# 	value = memory[pc + 2]
	# 	register[reg_num] = value
	# 	pc += 3
	# elif ir == PRINT_REG:
	# 	reg_num = memory[pc + 1]
	# 	print(register[reg_num])
	# 	pc += 2
	# elif ir == ADD:
	# 	reg_num1 = memory[pc + 1]
	# 	reg_num2 = memory[pc + 2]
	# 	register[reg_num1] += register[reg_num2]
	# 	pc += 3
	# elif ir == HALT:
	# 	running = False
	# 	pc += 1
	# else:
	# 	print(f'Unknown instruction {ir} at address {pc}')
	# 	sys.exit(1)


'''
A Branch Table is a way for us to call functions in constant time using an object.
'''

def fun1(x, y):
    print("fun1")
def fun2():
    print("fun2")
def fun3():
    print("fun3")
def fun4():
    print("fun4")

def call_fun(n):
    branch_table = {
        1: fun1,
        2: fun2,
        3: fun3,
        4: fun4,
    }

f = branch_table[n]
f(x, y)

call_fun(2, 5, 4)

'''
Bitwise Operations

We're checking individual bits.
'''

'''
Truth table
A   B   A and B
F   F     F
T   F     F
F   T     F
T   T     T

Bitwise Truth table
A   B   A & B
0   0     0
1   0     0
0   1     0
1   1     1

Bitwise Truth table
A   B   A | B
0   0     0
1   0     1
0   1     1
1   1     1

AND can act as a mask.
OR can be used to set bits.
'''

'''
Shifting

111001
011100
001110
000111
000011

Base 10, Decimal:
  vv
12345678

Shift 2
34567800

Shift 6
00000034


The user wants 34 out.

'''

