# Copyright 2018 Akifumi Fujita
#
# Licensed under the Apache License, Version 2.0 (the "License")
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

from . import rv32i
from . import util

class UnknownOp:
    def __str__(self):
        return "Unknown"

class OperandR:
    def __init__(self, insn):
        self.funct7 = util.pick(insn, 25, 7)
        self.rs2    = util.pick(insn, 20, 5)
        self.rs1    = util.pick(insn, 15, 5)
        self.funct3 = util.pick(insn, 12, 3)
        self.rd     = util.pick(insn,  7, 5)

class OperandI:
    def __init__(self, insn):
        self.imm    = util.sign_extend32(12, util.pick(insn, 20, 12))
        self.rs1    = util.pick(insn, 15, 5)
        self.funct3 = util.pick(insn, 12, 3)
        self.rd     = util.pick(insn, 7, 5)

class OperandI_CSR:
    def __init__(self, insn):
        self.csr    = util.pick(insn, 20, 12)
        self.zimm   = util.pick(insn, 15, 5)
        self.rs1    = util.pick(insn, 15, 5)
        self.funct3 = util.pick(insn, 12, 3)
        self.rd     = util.pick(insn, 7, 5)

class OperandS:
    def __init__(self, insn):
        self.imm    = util.sign_extend32(12, util.pick(insn, 25, 7) << 5 | util.pick(insn, 7, 5))
        self.rs2    = util.pick(insn, 20, 5)
        self.rs1    = util.pick(insn, 15, 5)
        self.funct3 = util.pick(insn, 12, 3)

class OperandB:
    def __init__(self, insn):
        self.imm =      util.sign_extend32(13, util.pick(insn, 31) << 12 | util.pick(insn, 7) << 11 | util.pick(insn, 25, 6) << 5 | util.pick(insn, 8, 4) << 1)
        self.rs2 =      util.pick(insn, 20, 5)
        self.rs1 =      util.pick(insn, 15, 5)
        self.funct3 =   util.pick(insn, 12, 3)

class OperandU:
    def __init__(self, insn):
        self.imm =      util.pick(insn, 12, 20) << 12,
        self.rd =       util.pick(insn, 7, 5)

class OperandJ:
    def __init__(self, insn):
        self.imm =      util.pick(insn, 31) << 20 | util.pick(insn, 21, 10) << 1 | util.pick(insn, 20) << 11 | util.pick(insn, 12, 8) << 12,
        self.rd =       util.pick(insn, 7, 5)

def decode(insn):
    opcode = util.pick(insn, 0, 7)

    r = OperandR(insn)
    i = OperandI(insn)
    i_csr = OperandI_CSR(insn)
    s = OperandS(insn)
    b = OperandB(insn)
    u = OperandU(insn)
    j = OperandJ(insn)

    if opcode == 0b0110111:
        return rv32i.LUI(u.rd, u.imm)
    elif opcode == 0b0010111:
        return rv32i.AUIPC(u.rd, u.imm)
    elif opcode == 0b1101111:
        return rv32i.JAL(j.rd, j.imm)
    elif opcode == 0b1100111:
        return rv32i.JALR(i.rd, i.rs1, i.imm)
    elif opcode == 0b1100011:
        if b.funct3 == 0b000:
            return rv32i.BEQ(b.rs1, b.rs2, b.imm)
        elif b.funct3 == 0b001:
            return rv32i.BNE(b.rs1, b.rs2, b.imm)
        elif b.funct3 == 0b100:
            return rv32i.BLT(b.rs1, b.rs2, b.imm)
        elif b.funct3 == 0b101:
            return rv32i.BGE(b.rs1, b.rs2, b.imm)
        elif b.funct3 == 0b110:
            return rv32i.BLTU(b.rs1, b.rs2, b.imm)
        elif b.funct3 == 0b111:
            return rv32i.BGEU(b.rs1, b.rs2, b.imm)
        else:
            raise Exception(f"Failed to decode insn 0x{insn:08x}")
    elif opcode == 0b0000011:
        if i.funct3 == 0b000:
            return rv32i.LB(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b001:
            return rv32i.LH(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b010:
            return rv32i.LW(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b100:
            return rv32i.LBU(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b101:
            return rv32i.LHU(i.rd, i.rs1, i.imm)
        else:
            raise Exception(f"Failed to decode insn 0x{insn:08x}")
    elif opcode == 0b0100011:
        if s.funct3 == 0b000:
            return rv32i.SB(s.rs1, s.rs2, s.imm)
        elif s.funct3 == 0b001:
            return rv32i.SH(s.rs1, s.rs2, s.imm)
        elif s.funct3 == 0b010:
            return rv32i.SW(s.rs1, s.rs2, s.imm)
        else:
            raise Exception(f"Failed to decode insn 0x{insn:08x}")
    elif opcode == 0b0010011:
        if i.funct3 == 0b000:
            return rv32i.ADDI(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b001 and r.funct7 == 0b0000000:
            return rv32i.SLLI(r.rd, r.rs1, r.rs2)
        elif i.funct3 == 0b010:
            return rv32i.SLTI(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b011:
            return rv32i.SLTIU(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b100:
            return rv32i.XORI(i.rd, i.rs1, i.imm)
        elif r.funct3 == 0b101 and r.funct7 == 0b0000000:
            return rv32i.SRLI(r.rd, r.rs1, r.rs2)
        elif r.funct3 == 0b101 and r.funct7 == 0b0100000:
            return rv32i.SRAI(r.rd, r.rs1, r.rs2)
        elif i.funct3 == 0b110:
            return rv32i.ORI(i.rd, i.rs1, i.imm)
        elif i.funct3 == 0b111:
            return rv32i.ANDI(i.rd, i.rs1, i.imm)
        else:
            raise Exception(f"Failed to decode insn 0x{insn:08x}")
    elif opcode == 0b0110011:
        if r.funct7 == 0b0000000 and r.funct3 == 0b000:
            return rv32i.ADD(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0000000 and r.funct3 == 0b001:
            return rv32i.SLL(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0000000 and r.funct3 == 0b010:
            return rv32i.SLT(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0000000 and r.funct3 == 0b011:
            return rv32i.SLTU(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0000000 and r.funct3 == 0b100:
            return rv32i.XOR(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0000000 and r.funct3 == 0b101:
            return rv32i.SRL(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0000000 and r.funct3 == 0b110:
            return rv32i.OR(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0000000 and r.funct3 == 0b111:
            return rv32i.AND(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0100000 and r.funct3 == 0b000:
            return rv32i.SUB(r.rd, r.rs1, r.rs2)
        elif r.funct7 == 0b0100000 and r.funct3 == 0b001:
            return rv32i.SRA(r.rd, r.rs1, r.rs2)
        else:
            raise Exception(f"Failed to decode insn 0x{insn:08x}")
    elif opcode == 0b0001111:
        if i.rs1 == 0b00000 and i.funct3 == 0b000 and i.rd == 0b00000 and util.pick(insn, 28, 4) == 0b0000:
            return rv32i.FENCE(util.pick(insn, 24, 4), util.pick(insn, 20, 4))
        elif i.rs1 == 0b00000 and i.funct3 == 0b001 and i.rd == 0b00000 and i.imm == 0b0000_0000_0000:
            return rv32i.FENCE_I()
        else:
            raise Exception(f"Failed to decode insn 0x{insn:08x}")
    elif opcode == 0b1110011:
        if i.imm == 0b0000_0000_0010 and r.rs1 == 0b00000 and r.funct3 == 0b000 and r.rd == 0b00000:
            return rv32i.URET()
        elif i.imm == 0b0001_0000_0010 and r.rs1 == 0b00000 and r.funct3 == 0b000 and r.rd == 0b00000:
            return rv32i.SRET()
        elif i.imm == 0b0011_0000_0010 and r.rs1 == 0b00000 and r.funct3 == 0b000 and r.rd == 0b00000:
            return rv32i.MRET()
        elif i.imm == 0b0001_0000_0101 and r.rs1 == 0b00000 and r.funct3 == 0b000 and r.rd == 0b00000:
            return rv32i.WFI()
        elif i.imm == 0b0001_0000_0101 and r.rs1 == 0b00000 and r.funct3 == 0b000 and r.rd == 0b00000:
            return rv32i.SFENCE_VMA(r.rs1, r.rs2)
        elif i.imm == 0b0000_0000_0000 and i.rs1 == 0b00000 and i.funct3 == 0b000 and i.rd == 0b00000:
            return rv32i.ECALL()
        elif i.imm == 0b0000_0000_0001 and i.rs1 == 0b00000 and i.funct3 == 0b000 and i.rd == 0b00000:
            return rv32i.EBREAK()
        elif i_csr.funct3 == 0b001:
            return rv32i.CSRRW(i_csr.csr, i_csr.rd, i_csr.rs1)
        elif i_csr.funct3 == 0b010:
            return rv32i.CSRRS(i_csr.csr, i_csr.rd, i_csr.rs1)
        elif i_csr.funct3 == 0b011:
            return rv32i.CSRRC(i_csr.csr, i_csr.rd, i_csr.rs1)
        elif i_csr.funct3 == 0b101:
            return rv32i.CSRRWI(i_csr.csr, i_csr.rd, i_csr.zimm)
        elif i_csr.funct3 == 0b110:
            return rv32i.CSRRSI(i_csr.csr, i_csr.rd, i_csr.zimm)
        elif i_csr.funct3 == 0b111:
            return rv32i.CSRRCI(i_csr.csr, i_csr.rd, i_csr.zimm)
        else:
            raise Exception(f"Failed to decode insn 0x{insn:08x}")
    else:
        raise Exception(f"Failed to decode insn 0x{insn:08x}")
