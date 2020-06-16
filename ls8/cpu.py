"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.cpu = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True
        self.branch_table = {}
        self.branch_table[fun1] = 

    def ram_read(self, pc): # Program Counter, index of the current instruction
        print(self.cpu[self.pc])
        self.pc += 1

    def ram_write(self, pc, value):
        self.cpu[self.pc] = value
        self.pc += 2

    def load(self):
        """Load a program into memory."""
        filename = sys.argv[1]
        with open(f'/Users/vinnihoke/git-projects/classes/lambda/cs/Computer-Architecture/ls8/examples/{filename}') as f:
            for address, line in enumerate(f):
                line = line.split("#")
                try:
                    v = int(line[0])
                except ValueError:
                    continue
                self.cpu[address] = v


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        ir = self.cpu[self.pc] # Stands for internal register

        while self.running:
            branch_table = {
                1: self.ram_read(ir),
                2: self.ram_write(ir, value)
            }

            branch_table[ir]
        
