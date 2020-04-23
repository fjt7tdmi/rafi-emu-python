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

class Memory:
    "Memory emulation class"

    CAPACITY = 64 * 1024

    data = bytearray(CAPACITY)

    def load(self, path):
        with open(path, mode='rb') as f:
            data = f.read()
            if len(data) > len(self.data):
                raise Exception(f"Size of '{path}' ({len(data)}) is larger than memory size ({len(self.data)}).")
            self.data[0:len(data)] = data[0:len(data)]

    def read_uint8(self, addr):
        return int.from_bytes(self.data[addr:addr+1], byteorder='little', signed=False)

    def read_uint16(self, addr):
        return int.from_bytes(self.data[addr:addr+2], byteorder='little', signed=False)

    def read_uint32(self, addr):
        return int.from_bytes(self.data[addr:addr+4], byteorder='little', signed=False)

    def write_uint8(self, addr, value):
        x = value.to_bytes(byteorder='little', signed=False)
        for i in range(1):
            self.data[addr + i] = x[i]

    def write_uint16(self, addr, value):
        x = value.to_bytes(byteorder='little', signed=False)
        for i in range(2):
            self.data[addr + i] = x[i]

    def write_uint32(self, addr, value):
        x = value.to_bytes(byteorder='little', signed=False)
        for i in range(4):
            self.data[addr + i] = x[i]
