# Copyright 2018 Akifumi Fujita
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fixedint import *
from . import rv
from . import util
from . import cpu

class Op:
    def execute(self, cpuState, bus):
        pass

    def post_check_trap(self, cpuState):
        return None

class LUI(Op):
    def __init__(self, rd, imm):
        self.rd = rd
        self.imm = imm

    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"lui {rd},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = self.imm

class AUIPC(Op):
    def __init__(self, rd, imm):
        self.rd = rd
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"auipc {rd},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = cpuState.pc + self.imm

class JAL(Op):
    def __init__(self, rd, imm):
        self.rd = rd
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"jal {rd},{imm}"
    
    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        next_pc = cpuState.next_pc

        cpuState.next_pc = cpuState.pc + self.imm
        x[self.rd] = next_pc

class JALR(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"jalr {rd},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        next_pc = cpuState.next_pc

        cpuState.next_pc = x[self.rs1] + self.imm
        x[self.rd] = next_pc

class BEQ(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"beqz {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"beqz {rs1}, #{imm}"
        else:
            return f"beq {rs1}, {rs2}, #{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg

        if x[self.rs1] == x[self.rs2]:
            cpuState.next_pc = cpuState.pc + self.imm

class BNE(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"bnez {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"bnez {rs1}, #{imm}"
        else:
            return f"bne {rs1}, {rs2}, #{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg

        if x[self.rs1] != x[self.rs2]:
            cpuState.next_pc = cpuState.pc + self.imm

class BLT(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"bltz {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"bltz {rs1}, #{imm}"
        else:
            return f"blt {rs1}, {rs2}, #{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg

        if Int32(x[self.rs1]) < Int32(x[self.rs2]):
            cpuState.next_pc = cpuState.pc + self.imm

class BGE(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"bgez {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"bgez {rs1}, #{imm}"
        else:
            return f"bge {rs1}, {rs2}, #{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg

        if Int32(x[self.rs1]) >= Int32(x[self.rs2]):
            cpuState.next_pc = cpuState.pc + self.imm

class BLTU(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"bltu {rs1}, {rs2}, #{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg

        if x[self.rs1] < x[self.rs2]:
            cpuState.next_pc = cpuState.pc + self.imm

class BGEU(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"bgeu {rs1}, {rs2}, #{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg

        if x[self.rs1] >= x[self.rs2]:
            cpuState.next_pc = cpuState.pc + self.imm

class LB(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lb {rd},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = bus.read_uint8(addr)

        x[self.rd] = util.sign_extend32(8, value)

class LH(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lh {rd},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = bus.read_uint16(addr)

        x[self.rd] = util.sign_extend32(16, value)

class LW(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lw {rd},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = bus.read_uint32(addr)

        x[self.rd] = value

class LBU(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lbu {rd},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = bus.read_uint8(addr)

        x[self.rd] = util.zero_extend32(8, value)

class LHU(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lhu {rd},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = bus.read_uint16(addr)

        x[self.rd] = util.zero_extend32(16, value)

class SB(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"sb {rs2},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = x[self.rs2]
        
        bus.write_uint8(addr, value)

class SH(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"sh {rs2},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = x[self.rs2]
        
        bus.write_uint16(addr, value)

class SW(Op):
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"sw {rs2},{imm}({rs1})"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        addr = x[self.rs1] + self.imm
        value = x[self.rs2]
        
        bus.write_uint32(addr, value)

class ADDI(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"addi {rd},{rs1},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] + self.imm

class SLTI(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"slti {rd},{rs1},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = UInt32(1) if Int32(x[self.rs1]) < Int32(self.imm) else UInt32(0)

class SLTIU(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"slti {rd},{rs1},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = UInt32(1) if x[self.rs1] < self.imm else UInt32(0)

class XORI(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"xori {rd},{rs1},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] ^ self.imm

class ORI(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"ori {rd},{rs1},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] | self.imm

class ANDI(Op):
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"andi {rd},{rs1},{imm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] & self.imm

class SLLI(Op):
    def __init__(self, rd, rs1, shamt):
        self.rd = rd
        self.rs1 = rs1
        self.shamt = shamt
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        shamt = self.shamt
        return f"slli {rd},{rs1},0x{shamt:x}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] << self.shamt

class SRLI(Op):
    def __init__(self, rd, rs1, shamt):
        self.rd = rd
        self.rs1 = rs1
        self.shamt = shamt
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        shamt = self.shamt
        return f"srli {rd},{rs1},0x{shamt:x}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] >> self.shamt

class SRAI(Op):
    def __init__(self, rd, rs1, shamt):
        self.rd = rd
        self.rs1 = rs1
        self.shamt = shamt
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        shamt = self.shamt
        return f"srai {rd},{rs1},0x{shamt:x}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = UInt32(Int32(x[self.rs1]) >> self.shamt)

class ADD(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"add {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = UInt32(x[self.rs1] + x[self.rs2])

class SUB(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"sub {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = UInt32(x[self.rs1] - x[self.rs2])

class SLL(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"sll {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] << (x[self.rs2] & 0x1f)

class SLT(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"slt {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = UInt32(1) if Int32(x[self.rs1]) < Int32(x[self.rs2]) else UInt32(0)

class SLTU(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"sltu {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = UInt32(1) if x[self.rs1] < x[self.rs2] else UInt32(0)

class XOR(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"xor {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] ^ x[self.rs2]

class SRL(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"srl {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] >> (x[self.rs2] & 0x1f)

class SRA(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"sra {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg

        x[self.rd] = UInt32(Int32(x[self.rs1]) >> (x[self.rs2] & 0x1f))

class OR(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"or {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] | x[self.rs2]

class AND(Op):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"and {rd},{rs1},{rs2}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        x[self.rd] = x[self.rs1] & x[self.rs2]

class FENCE(Op):
    def __init__(self, pred, succ):
        self.pred = pred
        self.succ = succ

    def __str__(self):
        return "fence"

class FENCE_I(Op):
    def __str__(self):
        return "fence.i"

class ECALL(Op):
    def __str__(self):
        return "ecall"

    def post_check_trap(self, cpuState):
        return cpu.EnvironmentCallFromMachineException(cpuState.pc)

class EBREAK(Op):
    def __str__(self):
        return "ebreak"

    def post_check_trap(self, cpuState):
        return cpu.BreakpointException(cpuState.pc)

class CSRRW(Op):
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.rs1 = rs1
    
    def __str__(self):
        csr = rv.CSR_NAMES[self.csr]
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        if rd == 0:
            return f"csrw {csr},{rs1}"
        else:
            return f"csrrw {rd},{csr},{rs1}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        csr = cpuState.csr
        value = csr[self.csr]

        csr[self.csr] = x[self.rs1]
        x[self.rd] = value

class CSRRS(Op):
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.rs1 = rs1
    
    def __str__(self):
        csr = rv.CSR_NAMES[self.csr]
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        if rs1 == 0:
            return f"csrr {rd},{csr}"
        elif rd == 0:
            return f"csrr {csr},{rs1}"
        else:
            return f"csrrs {rd},{csr},{rs1}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        csr = cpuState.csr
        value = csr[self.csr]

        csr[self.csr] = value | x[self.rs1]
        x[self.rd] = value

class CSRRC(Op):
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.rs1 = rs1
    
    def __str__(self):
        csr = rv.CSR_NAMES[self.csr]
        rd = rv.INT_REG_NAMES[self.rd]
        rs1 = rv.INT_REG_NAMES[self.rs1]
        if rd == 0:
            return f"csrc {csr},{rs1}"
        else:
            return f"csrrc {rd},{csr},{rs1}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        value = cpuState.csr[self.csr]

        cpuState.csr[self.csr] = ~value & x[self.rs1]
        x[self.rd] = value

class CSRRWI(Op):
    def __init__(self, csr, rd, zimm):
        self.csr = csr
        self.rd = rd
        self.zimm = zimm
    
    def __str__(self):
        csr = rv.CSR_NAMES[self.csr]
        rd = rv.INT_REG_NAMES[self.rd]
        zimm = self.zimm
        if rd == 0:
            return f"csrwi {csr},{zimm}"
        else:
            return f"csrrwi {rd},{csr},{zimm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        csr = cpuState.csr

        value = csr[self.csr]
        csr[self.csr] = self.zimm
        x[self.rd] = value

class CSRRSI(Op):
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.zimm = zimm
    
    def __str__(self):
        csr = rv.CSR_NAMES[self.csr]
        rd = rv.INT_REG_NAMES[self.rd]
        zimm = self.zimm
        if rd == 0:
            return f"csrsi {csr},{zimm}"
        else:
            return f"csrrsi {rd},{csr},{zimm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        csr = cpuState.csr

        value = csr[self.csr]
        csr[self.csr] = value | self.zimm
        x[self.rd] = value

class CSRRCI(Op):
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.zimm = zimm
    
    def __str__(self):
        csr = rv.CSR_NAMES[self.csr]
        rd = rv.INT_REG_NAMES[self.rd]
        zimm = self.zimm
        if rd == 0:
            return f"csrci {csr},{zimm}"
        else:
            return f"csrrci {rd},{csr},{zimm}"

    def execute(self, cpuState, bus):
        x = cpuState.int_reg
        csr = cpuState.csr

        value = csr[self.csr]
        csr[self.csr] = ~value & self.zimm
        x[self.rd] = value

class URET(Op):
    def __str__(self):
        return "uret"

    def post_check_trap(self, cpuState):
        return cpu.TrapReturn(cpuState.pc)

class SRET(Op):
    def __str__(self):
        return "sret"

    def post_check_trap(self, cpuState):
        return cpu.TrapReturn(cpuState.pc)

class MRET(Op):
    def __str__(self):
        return "mret"

class WFI(Op):
    def __str__(self):
        return "wfi"

class SFENCE_VMA(Op):
    def __init__(self, rs1, rs2):
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rs1 = rv.INT_REG_NAMES[self.rs1]
        rs2 = rv.INT_REG_NAMES[self.rs2]
        return f"sfence.vma {rs1},{rs2}"
