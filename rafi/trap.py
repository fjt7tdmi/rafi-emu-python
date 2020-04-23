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

class TrapType(Enum):
    INTERRUPT = 0
    EXCEPTION = 1
    RETURN = 2

class InterruptType(Enum):
    SOFTWARE_U = 0
    SOFTWARE_S = 1
    SOFTWARE_M = 3
    TIMER_U = 4
    TIMER_S = 5
    TIMER_M = 7
    EXTERNAL_U = 8
    EXTERNAL_S = 9
    EXTERNAL_M = 11

class ExceptionType(Enum):
    INSN_ADDR_MISALIGNED = 0
    INSN_ACCESS_FAULT = 1
    ILLEGAL_INSN = 2
    BREAKPOINT = 3
    LOAD_ADDR_MISALIGNED = 4
    LOAD_ACCESS_FAULT = 5
    STORE_ADDR_MISALIGNED = 6
    STORE_ACCESS_FAULT = 7
    ECALL_FROM_U = 8
    ECALL_FROM_S = 9
    ECALL_FROM_M = 11
    INSN_PAGE_FAULT = 12
    LOAD_PAGE_FAULT = 13
    STORE_PAGE_FAULT = 15

