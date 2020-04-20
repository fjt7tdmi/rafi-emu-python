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

from . import util

class LUI:
    def __init__(self, rd, imm):
        self.rd = rd
        self.imm = imm

    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"lui {rd},{imm}"

class AUIPC:
    def __init__(self, rd, imm):
        self.rd = rd
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"auipc {rd},{imm}"

class JAL:
    def __init__(self, rd, imm):
        self.rd = rd
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"jal {rd},{imm}"

class JALR:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        imm = self.imm
        return f"jalr {rd},{imm}"

class BEQ:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"beqz {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"beqz {rs1}, #{imm}"
        else:
            return f"beq {rs1}, {rs2}, #{imm}"

class BNE:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"bnez {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"bnez {rs1}, #{imm}"
        else:
            return f"bne {rs1}, {rs2}, #{imm}"

class BLT:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"bltz {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"bltz {rs1}, #{imm}"
        else:
            return f"blt {rs1}, {rs2}, #{imm}"

class BGE:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        if self.rs1 == 0:
            return f"bgez {rs2}, #{imm}"
        elif self.rs2 == 0:
            return f"bgez {rs1}, #{imm}"
        else:
            return f"bge {rs1}, {rs2}, #{imm}"

class BLTU:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"bltu {rs1}, {rs2}, #{imm}"

class BGEU:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"bgeu {rs1}, {rs2}, #{imm}"

class LB:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lb {rd},{imm}({rs1})"

class LH:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lh {rd},{imm}({rs1})"

class LW:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lw {rd},{imm}({rs1})"

class LBU:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lbu {rd},{imm}({rs1})"

class LHU:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"lhu {rd},{imm}({rs1})"

class SB:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"sb {rs2},{imm}({rs1})"

class SH:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"sh {rs2},{imm}({rs1})"

class SW:
    def __init__(self, rs1, rs2, imm):
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        imm = self.imm
        return f"sw {rs2},{imm}({rs1})"

class ADDI:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"addi {rd},{rs1},{imm}"

class SLTI:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"slti {rd},{rs1},{imm}"

class SLTIU:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"slti {rd},{rs1},{imm}"

class XORI:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"xori {rd},{rs1},{imm}"

class ORI:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"ori {rd},{rs1},{imm}"

class ANDI:
    def __init__(self, rd, rs1, imm):
        self.rd = rd
        self.rs1 = rs1
        self.imm = imm
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        imm = self.imm
        return f"andi {rd},{rs1},{imm}"

class SLLI:
    def __init__(self, rd, rs1, shamt):
        self.rd = rd
        self.rs1 = rs1
        self.shamt = shamt
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        shamt = self.shamt
        return f"slli {rd},{rs1},0x{shamt:x}"

class SRLI:
    def __init__(self, rd, rs1, shamt):
        self.rd = rd
        self.rs1 = rs1
        self.shamt = shamt
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        shamt = self.shamt
        return f"srli {rd},{rs1},0x{shamt:x}"

class SRAI:
    def __init__(self, rd, rs1, shamt):
        self.rd = rd
        self.rs1 = rs1
        self.shamt = shamt
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        shamt = self.shamt
        return f"srai {rd},{rs1},0x{shamt:x}"

class ADD:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"add {rd},{rs1},{rs2}"

class SUB:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"sub {rd},{rs1},{rs2}"

class SLL:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"sll {rd},{rs1},{rs2}"

class SLT:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"slt {rd},{rs1},{rs2}"

class SLTU:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"sltu {rd},{rs1},{rs2}"

class XOR:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"xor {rd},{rs1},{rs2}"

class SRL:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"srl {rd},{rs1},{rs2}"

class SRA:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"sra {rd},{rs1},{rs2}"

class OR:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"or {rd},{rs1},{rs2}"

class AND:
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"and {rd},{rs1},{rs2}"

class FENCE:
    def __init__(self, pred, succ):
        self.pred = pred
        self.succ = succ

    def __str__(self):
        return "fence"

class FENCE_I:
    def __str__(self):
        return "fence.i"

class ECALL:
    def __str__(self):
        return "ecall"

class EBREAK:
    def __str__(self):
        return "ebreak"

class CSRRW:
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.rs1 = rs1
    
    def __str__(self):
        csr = util.CSR_NAMES[self.csr]
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        if rd == 0:
            return f"csrw {csr},{rs1}"
        else:
            return f"csrrw {rd},{csr},{rs1}"

class CSRRS:
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.rs1 = rs1
    
    def __str__(self):
        csr = util.CSR_NAMES[self.csr]
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        if rs1 == 0:
            return f"csrr {rd},{csr}"
        elif rd == 0:
            return f"csrr {csr},{rs1}"
        else:
            return f"csrrs {rd},{csr},{rs1}"

class CSRRC:
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.rs1 = rs1
    
    def __str__(self):
        csr = util.CSR_NAMES[self.csr]
        rd = util.INT_REG_NAMES[self.rd]
        rs1 = util.INT_REG_NAMES[self.rs1]
        if rd == 0:
            return f"csrc {csr},{rs1}"
        else:
            return f"csrrc {rd},{csr},{rs1}"

class CSRRWI:
    def __init__(self, csr, rd, zimm):
        self.csr = csr
        self.rd = rd
        self.zimm = zimm
    
    def __str__(self):
        csr = util.CSR_NAMES[self.csr]
        rd = util.INT_REG_NAMES[self.rd]
        zimm = self.zimm
        if rd == 0:
            return f"csrwi {csr},{zimm}"
        else:
            return f"csrrwi {rd},{csr},{zimm}"

class CSRRSI:
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.zimm = zimm
    
    def __str__(self):
        csr = util.CSR_NAMES[self.csr]
        rd = util.INT_REG_NAMES[self.rd]
        zimm = self.zimm
        if rd == 0:
            return f"csrsi {csr},{zimm}"
        else:
            return f"csrrsi {rd},{csr},{zimm}"

class CSRRCI:
    def __init__(self, csr, rd, rs1):
        self.csr = csr
        self.rd = rd
        self.zimm = zimm
    
    def __str__(self):
        csr = util.CSR_NAMES[self.csr]
        rd = util.INT_REG_NAMES[self.rd]
        zimm = self.zimm
        if rd == 0:
            return f"csrci {csr},{zimm}"
        else:
            return f"csrrci {rd},{csr},{zimm}"

class URET:
    def __str__(self):
        return "uret"

class SRET:
    def __str__(self):
        return "sret"

class MRET:
    def __str__(self):
        return "mret"

class WFI:
    def __str__(self):
        return "wfi"

class SFENCE_VMA:
    def __init__(self, rs1, rs2):
        self.rs1 = rs1
        self.rs2 = rs2
    
    def __str__(self):
        rs1 = util.INT_REG_NAMES[self.rs1]
        rs2 = util.INT_REG_NAMES[self.rs2]
        return f"sfence.vma {rs1},{rs2}"
