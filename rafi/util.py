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

INT_REG_NAMES = [
    "zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2",
    "s0", "s1", "a0", "a1", "a2", "a3", "a4", "a5",
    "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7",
    "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6",
]

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

def pick(insn, lsb, width=1):
    return abs((insn >> lsb) & ((1 << width) - 1))

def sign_extend(width, value, max_width):
    if width < 0:
        raise ValueError(f"Argument 'width' ({width}) must be positive integer.")
    if value < 0:
        raise ValueError(f"Argument 'value' ({value}) must be positive integer.")
    if max_width < 0:
        raise ValueError(f"Argument 'max_width' ({max_width}) must be positive integer.")

    sign = (value >> (width - 1)) & 0x1
    mask = (0x1 << width) - 1

    if sign == 0:
        return value & mask
    else:
        all_one = (1 << max_width) - 1
        return value | (all_one - mask)

def sign_extend32(width, value):
    return sign_extend(width, value, 32)

def sign_extend64(width, value):
    return sign_extend(width, value, 64)

def zero_extend(width, value):
    if width < 0:
        raise ValueError(f"Argument 'width' ({width}) must be positive integer.")
    if value < 0:
        raise ValueError(f"Argument 'value' ({value}) must be positive integer.")

    value = abs(value)
    mask = (0x1 << width) - 1

    return value & mask

def zero_extend32(width, value):
    return zero_extend(width, value)

def zero_extend64(width, value):
    return zero_extend(width, value)

