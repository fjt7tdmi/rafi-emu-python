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

