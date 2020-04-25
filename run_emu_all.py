#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import json
import os
import rafi
import sys

CONFIG_PATH = "./riscv_tests.json"
BINARY_DIR_PATH = "./rafi-prebuilt-binary/riscv-tests/isa"
MAX_CYCLE = 10000

configs = None
with open(CONFIG_PATH, "r") as f:
    configs = json.load(f)

failure_count = 0
for config in configs:
    path = os.path.join(BINARY_DIR_PATH, f"{config}.bin")
    try:
        print(f"{path}")
        rafi.run_emulation(path, MAX_CYCLE)
    except Exception as e:
        print(e)
        failure_count += 1

sys.exit(failure_count)
