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
from . import cpu
from . import mem
from . import rv
from . import rv32i
from . import util

# =============================================================================
# Decoder
#
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
        self.imm =      util.pick(insn, 12, 20) << 12
        self.rd =       util.pick(insn, 7, 5)

class OperandJ:
    def __init__(self, insn):
        self.imm =      util.sign_extend32(21, util.pick(insn, 31) << 20 | util.pick(insn, 21, 10) << 1 | util.pick(insn, 20) << 11 | util.pick(insn, 12, 8) << 12)
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
        elif r.funct7 == 0b0100000 and r.funct3 == 0b101:
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

# =============================================================================
# Bus
#
class Bus:
    def __init__(self, memory):
        self.memory = memory
    
    def get_memory_addr(self, addr):
        return addr - 0x8000_0000

    def read_uint8(self, addr):
        memory_addr = self.get_memory_addr(addr)
        return self.memory.read_uint8(memory_addr)

    def read_uint16(self, addr):
        memory_addr = self.get_memory_addr(addr)
        return self.memory.read_uint16(memory_addr)

    def read_uint32(self, addr):
        memory_addr = self.get_memory_addr(addr)
        return self.memory.read_uint32(memory_addr)

    def write_uint8(self, addr, value):
        memory_addr = self.get_memory_addr(addr)
        self.memory.write_uint8(memory_addr, value)

    def write_uint16(self, addr, value):
        memory_addr = self.get_memory_addr(addr)
        self.memory.write_uint16(memory_addr, value)

    def write_uint32(self, addr, value):
        memory_addr = self.get_memory_addr(addr)
        self.memory.write_uint32(memory_addr, value)

# =============================================================================
# Processor
#
class Processor:
    cpuState = cpu.CpuState()

    def __init__(self, bus):
        self.bus = bus
        self.cpuState.pc = 0x8000_0000

    def dump_cpu_state(self):
        for i in range(32):
            print(f"{rv.INT_REG_NAMES[i]} {self.cpuState.int_reg[i]:08x}")

    def process_cycle(self):
        # fetch
        insn = self.bus.read_uint32(self.cpuState.pc)
        self.cpuState.next_pc = self.cpuState.pc + 4

        # decode
        op = decode(insn)
        #print(f"{self.cpuState.pc:08x} {op}")

        # execute
        op.execute(self.cpuState, self.bus)
        trap = op.post_check_trap(self.cpuState)
        if trap is not None:
            self.process_trap(trap)

        # finalize
        self.cpuState.pc = self.cpuState.next_pc
    
    def process_trap(self, trap):
        if trap.trapType == cpu.TrapType.EXCEPTION:
            self.process_exception(trap)
        elif trap.trapType == cpu.TrapType.RETURN:
            self.process_trap_return(trap)
        else:
            raise Exception("Not implemented.")

    def process_exception(self, trap):
        mtvec = rv.MTVEC(self.read_csr(rv.CsrAddr.MTVEC))
        mstatus = rv.MSTATUS(self.read_csr(rv.CsrAddr.MSTATUS))

        mstatus.set_MPIE(mstatus.get_MIE())
        mstatus.set_MIE(UInt32(0))
        mstatus.set_MPP(UInt32(3)) # priv M

        self.write_csr(rv.CsrAddr.MSTATUS, mstatus.value)
        self.write_csr(rv.CsrAddr.MCAUSE, UInt32(trap.cause))
        self.write_csr(rv.CsrAddr.MEPC, UInt32(trap.pc))
        self.write_csr(rv.CsrAddr.MTVAL, UInt32(trap.trapValue))
        self.cpuState.next_pc = mtvec.get_BASE() * 4

    def process_trap_return(self, trap):
        mstatus = rv.MSTATUS(self.read_csr(rv.CsrAddr.MSTATUS))
        mepc = self.read_csr(rv.CsrAddr.MEPC)

        mstatus.set_MPP(UInt32(0))
        mstatus.set_MIE(mstatus.get_MPIE())

        self.write_csr(rv.CsrAddr.MSTATUS, mstatus.value)
        self.cpuState.next_pc = mepc

    def read_csr(self, csrAddr):
        return self.cpuState.csr[csrAddr.value]

    def write_csr(self, csrAddr, value):
        self.cpuState.csr[csrAddr.value] = value

# =============================================================================
# Emulator
#
class Emulator:
    HOST_IO_ADDR = 0x8000_1000

    def __init__(self):
        self.memory = mem.Memory()
        self.bus = Bus(self.memory)
        self.processor = Processor(self.bus)

    def load(self, path):
        self.memory.load(path)

    def run(self, maxCycle):
        for cycle in range(int(maxCycle)):
            self.processor.process_cycle()

            host_io_value = self.bus.read_uint32(self.HOST_IO_ADDR)
            if host_io_value == 1:
                print(f"HostIo: {host_io_value} (success)")
                return
            elif host_io_value != 0:
                print(f"HostIo: {host_io_value} (failure: testId={host_io_value // 2})")
                raise Exception(f"Host IO value is not 1.")
        
        raise Exception(f"Emulation hasn't finished within {maxCycle} cycles.")