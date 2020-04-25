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

from enum import Enum
from fixedint import *
from . import util

# =============================================================================
# General register definitions
#

INT_REG_NAMES = [
    "zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2",
    "s0", "s1", "a0", "a1", "a2", "a3", "a4", "a5",
    "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7",
    "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6",
]

# =============================================================================
# CSR definitions
#

class CsrAddr(Enum):
    USTATUS     = 0x000
    FFLAGS      = 0x001
    FRM         = 0x002
    FCSR        = 0x003
    UIE         = 0x004
    UTVEC       = 0x005
    USCRATCH    = 0x040
    UEPC        = 0x041
    UCAUSE      = 0x042
    UTVAL       = 0x043
    UIP         = 0x044

    SSTATUS     = 0x100
    SEDELEG     = 0x102
    SIDELEG     = 0x103
    SIE         = 0x104
    STVEC       = 0x105
    SCOUNTEREN  = 0x106
    SSCRATCH    = 0x140
    SEPC        = 0x141
    SCAUSE      = 0x142
    STVAL       = 0x143
    SIP         = 0x144

    MSTATUS     = 0x300
    MISA        = 0x301
    MEDELEG     = 0x302
    MIDELEG     = 0x303
    MIE         = 0x304
    MTVEC       = 0x305
    MCOUNTEREN  = 0x306
    MHPMEVENT0  = 0x320
    MHPMEVENT1  = 0x321
    MHPMEVENT2  = 0x322
    MHPMEVENT3  = 0x323
    MHPMEVENT4  = 0x324
    MHPMEVENT5  = 0x325
    MHPMEVENT6  = 0x326
    MHPMEVENT7  = 0x327
    MHPMEVENT8  = 0x328
    MHPMEVENT9  = 0x329
    MHPMEVENT10 = 0x32a
    MHPMEVENT11 = 0x32b
    MHPMEVENT12 = 0x32c
    MHPMEVENT13 = 0x32d
    MHPMEVENT14 = 0x32e
    MHPMEVENT15 = 0x32f
    MHPMEVENT16 = 0x330
    MHPMEVENT17 = 0x331
    MHPMEVENT18 = 0x332
    MHPMEVENT19 = 0x333
    MHPMEVENT20 = 0x334
    MHPMEVENT21 = 0x335
    MHPMEVENT22 = 0x336
    MHPMEVENT23 = 0x337
    MHPMEVENT24 = 0x338
    MHPMEVENT25 = 0x339
    MHPMEVENT26 = 0x33a
    MHPMEVENT27 = 0x33b
    MHPMEVENT28 = 0x33c
    MHPMEVENT29 = 0x33d
    MHPMEVENT30 = 0x33e
    MHPMEVENT31 = 0x33f
    MSCRATCH    = 0x340
    MEPC        = 0x341
    MCAUSE      = 0x342
    MTVAL       = 0x343
    MIP         = 0x344
    PMPCMG0     = 0x3a0
    PMPCMG1     = 0x3a1
    PMPCMG2     = 0x3a2
    PMPCMG3     = 0x3a3
    PMPADDR0    = 0x3b0
    PMPADDR1    = 0x3b1
    PMPADDR2    = 0x3b2
    PMPADDR3    = 0x3b3
    PMPADDR4    = 0x3b4
    PMPADDR5    = 0x3b5
    PMPADDR6    = 0x3b6
    PMPADDR7    = 0x3b7
    PMPADDR8    = 0x3b8
    PMPADDR9    = 0x3b9
    PMPADDR10   = 0x3ba
    PMPADDR11   = 0x3bb
    PMPADDR12   = 0x3bc
    PMPADDR13   = 0x3bd
    PMPADDR14   = 0x3be
    PMPADDR15   = 0x3bf

    TSELECT     = 0x7a0
    TDATA1      = 0x7a1
    TDATA2      = 0x7a2
    TDATA3      = 0x7a3
    DCSR        = 0x7b0
    DPC         = 0x7b1
    DSCRATCH    = 0x7b2

    MCYCLE          = 0xb00
    MTIME           = 0xb01
    MINSTRET        = 0xb02
    MHPMCOUNTER3    = 0xb03
    MHPMCOUNTER4    = 0xb04
    MHPMCOUNTER5    = 0xb05
    MHPMCOUNTER6    = 0xb06
    MHPMCOUNTER7    = 0xb07
    MHPMCOUNTER8    = 0xb08
    MHPMCOUNTER9    = 0xb09
    MHPMCOUNTER10   = 0xb0a
    MHPMCOUNTER11   = 0xb0b
    MHPMCOUNTER12   = 0xb0c
    MHPMCOUNTER13   = 0xb0d
    MHPMCOUNTER14   = 0xb0e
    MHPMCOUNTER15   = 0xb0f
    MCYCLEH         = 0xb80
    MTIMEH          = 0xb81
    MINSTRETH       = 0xb82
    MHPMCOUNTER3H   = 0xb83
    MHPMCOUNTER4H   = 0xb84
    MHPMCOUNTER5H   = 0xb85
    MHPMCOUNTER6H   = 0xb86
    MHPMCOUNTER7H   = 0xb87
    MHPMCOUNTER8H   = 0xb88
    MHPMCOUNTER9H   = 0xb89
    MHPMCOUNTER10H  = 0xb8a
    MHPMCOUNTER11H  = 0xb8b
    MHPMCOUNTER12H  = 0xb8c
    MHPMCOUNTER13H  = 0xb8d
    MHPMCOUNTER14H  = 0xb8e
    MHPMCOUNTER15H  = 0xb8f

    CYCLE           = 0xc00
    TIME            = 0xc01
    INSTRET         = 0xc02
    HPMCOUNTER3     = 0xc03
    HPMCOUNTER4     = 0xc04
    HPMCOUNTER5     = 0xc05
    HPMCOUNTER6     = 0xc06
    HPMCOUNTER7     = 0xc07
    HPMCOUNTER8     = 0xc08
    HPMCOUNTER9     = 0xc09
    HPMCOUNTER10    = 0xc0a
    HPMCOUNTER11    = 0xc0b
    HPMCOUNTER12    = 0xc0c
    HPMCOUNTER13    = 0xc0d
    HPMCOUNTER14    = 0xc0e
    HPMCOUNTER15    = 0xc0f
    CYCLEH          = 0xc80
    TIMEH           = 0xc81
    INSTRETH        = 0xc82
    HPMCOUNTER3H    = 0xc83
    HPMCOUNTER4H    = 0xc84
    HPMCOUNTER5H    = 0xc85
    HPMCOUNTER6H    = 0xc86
    HPMCOUNTER7H    = 0xc87
    HPMCOUNTER8H    = 0xc88
    HPMCOUNTER9H    = 0xc89
    HPMCOUNTER10H   = 0xc8a
    HPMCOUNTER11H   = 0xc8b
    HPMCOUNTER12H   = 0xc8c
    HPMCOUNTER13H   = 0xc8d
    HPMCOUNTER14H   = 0xc8e
    HPMCOUNTER15H   = 0xc8f

    MVENDORID       = 0xf11
    MARCHID         = 0xf12
    MIMPID          = 0xf13
    MHARTID         = 0xf14

CSR_NAMES = {
    0x000: "ustatus",
    0x001: "fflags",
    0x002: "frm",
    0x003: "fcsr",
    0x004: "uie",
    0x005: "utvec",
    0x040: "uscratch",
    0x041: "uepc",
    0x042: "ucause",
    0x043: "utval",
    0x044: "uip",

    0x100: "sstatus",
    0x102: "sedeleg",
    0x103: "sideleg",
    0x104: "sie",
    0x105: "stvec",
    0x106: "scounteren",
    0x140: "sscratch",
    0x141: "sepc",
    0x142: "scause",
    0x143: "stval",
    0x144: "sip",
    0x180: "satp",

    0x300: "mstatus",
    0x301: "misa",
    0x302: "medeleg",
    0x303: "mideleg",
    0x304: "mie",
    0x305: "mtvec",
    0x306: "mcounteren",

    0x320: "mhpmevent0",
    0x321: "mhpmevent1",
    0x322: "mhpmevent2",
    0x323: "mhpmevent3",
    0x324: "mhpmevent4",
    0x325: "mhpmevent5",
    0x326: "mhpmevent6",
    0x327: "mhpmevent7",
    0x328: "mhpmevent8",
    0x329: "mhpmevent9",
    0x32a: "mhpmevent10",
    0x32b: "mhpmevent11",
    0x32c: "mhpmevent12",
    0x32d: "mhpmevent13",
    0x32e: "mhpmevent14",
    0x32f: "mhpmevent15",
    0x330: "mhpmevent16",
    0x331: "mhpmevent17",
    0x332: "mhpmevent18",
    0x333: "mhpmevent19",
    0x334: "mhpmevent20",
    0x335: "mhpmevent21",
    0x336: "mhpmevent22",
    0x337: "mhpmevent23",
    0x338: "mhpmevent24",
    0x339: "mhpmevent25",
    0x33a: "mhpmevent26",
    0x33b: "mhpmevent27",
    0x33c: "mhpmevent28",
    0x33d: "mhpmevent29",
    0x33e: "mhpmevent30",
    0x33f: "mhpmevent31",

    0x340: "mscratch",
    0x341: "mepc",
    0x342: "mcause",
    0x343: "mtval",
    0x344: "mip",

    0x3a0: "pmpcfg0",
    0x3a1: "pmpcfg1",
    0x3a2: "pmpcfg2",
    0x3a3: "pmpcfg3",

    0x3b0: "pmpaddr0",
    0x3b1: "pmpaddr1",
    0x3b2: "pmpaddr2",
    0x3b3: "pmpaddr3",
    0x3b4: "pmpaddr4",
    0x3b5: "pmpaddr5",
    0x3b6: "pmpaddr6",
    0x3b7: "pmpaddr7",
    0x3b8: "pmpaddr8",
    0x3b9: "pmpaddr9",
    0x3ba: "pmpaddr10",
    0x3bb: "pmpaddr11",
    0x3bc: "pmpaddr12",
    0x3bd: "pmpaddr13",
    0x3be: "pmpaddr14",
    0x3bf: "pmpaddr15",

    0x7a0: "tselect",
    0x7a1: "tdata1",
    0x7a2: "tdata2",
    0x7a3: "tdata3",
    0x7b0: "dcsr",
    0x7b1: "dpc",
    0x7b2: "dscratch",

    0xb00: "mcycle",
    0xb01: "mtime",
    0xb02: "minstret",
    0xb03: "mhpmcounter3",
    0xb04: "mhpmcounter4",
    0xb05: "mhpmcounter5",
    0xb06: "mhpmcounter6",
    0xb07: "mhpmcounter7",
    0xb08: "mhpmcounter8",
    0xb09: "mhpmcounter9",
    0xb0a: "mhpmcounter10",
    0xb0b: "mhpmcounter11",
    0xb0c: "mhpmcounter12",
    0xb0d: "mhpmcounter13",
    0xb0e: "mhpmcounter14",
    0xb0f: "mhpmcounter15",

    0xb80: "mcycleh",
    0xb81: "mtimeh",
    0xb82: "minstreth",
    0xb83: "mhpmcounter3h",
    0xb84: "mhpmcounter4h",
    0xb85: "mhpmcounter5h",
    0xb86: "mhpmcounter6h",
    0xb87: "mhpmcounter7h",
    0xb88: "mhpmcounter8h",
    0xb89: "mhpmcounter9h",
    0xb8a: "mhpmcounter10h",
    0xb8b: "mhpmcounter11h",
    0xb8c: "mhpmcounter12h",
    0xb8d: "mhpmcounter13h",
    0xb8e: "mhpmcounter14h",
    0xb8f: "mhpmcounter15h",

    0xc00: "cycle",
    0xc01: "time",
    0xc02: "instret",
    0xc03: "hpmcounter3",
    0xc04: "hpmcounter4",
    0xc05: "hpmcounter5",
    0xc06: "hpmcounter6",
    0xc07: "hpmcounter7",
    0xc08: "hpmcounter8",
    0xc09: "hpmcounter9",
    0xc0a: "hpmcounter10",
    0xc0b: "hpmcounter11",
    0xc0c: "hpmcounter12",
    0xc0d: "hpmcounter13",
    0xc0e: "hpmcounter14",
    0xc0f: "hpmcounter15",

    0xc80: "cycleh",
    0xc81: "timeh",
    0xc82: "instreth",
    0xc83: "hpmcounter3h",
    0xc84: "hpmcounter4h",
    0xc85: "hpmcounter5h",
    0xc86: "hpmcounter6h",
    0xc87: "hpmcounter7h",
    0xc88: "hpmcounter8h",
    0xc89: "hpmcounter9h",
    0xc8a: "hpmcounter10h",
    0xc8b: "hpmcounter11h",
    0xc8c: "hpmcounter12h",
    0xc8d: "hpmcounter13h",
    0xc8e: "hpmcounter14h",
    0xc8f: "hpmcounter15h",

    0xf11: "mvendorid",
    0xf12: "marchid",
    0xf13: "mimpid",
    0xf14: "mhartid",
}

class MSTATUS(util.BitField32):
    def get_MPP(self):
        return self.get_value(12, 11)
    
    def set_MPP(self, value):
        self.set_value(value, 12, 11)

    def get_MPIE(self):
        return self.get_bit(7)
    
    def set_MPIE(self, value):
        self.set_bit(value, 7)

    def get_MIE(self):
        return self.get_bit(3)
    
    def set_MIE(self, value):
        self.set_bit(value, 3)

class MTVEC(util.BitField32):
    def get_BASE(self):
        return self.get_value(31, 2)
    
    def set_BASE(self, value):
        self.set_value(value, 31, 2)

    def get_MODE(self):
        return self.get_value(1, 0)
    
    def set_MODE(self, value):
        self.set_value(value, 1, 0)
