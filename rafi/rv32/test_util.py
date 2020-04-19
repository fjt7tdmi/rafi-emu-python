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

import util
import unittest

class TestUtil(unittest.TestCase):
    def test_pick(self):
        self.assertEqual(0x34, util.pick(0x12345678, 16, 8))

    def test_sign_extend(self):
        self.assertEqual(0xffff8888, util.sign_extend32(16, 0xfff08888))
        self.assertEqual(0x00008888, util.sign_extend32(17, 0xfff08888))

    def test_zero_extend(self):
        self.assertEqual(0x00008888, util.zero_extend32(16, 0xfff08888))
        self.assertEqual(0x00008888, util.zero_extend32(17, 0xfff08888))

if __name__ == '__main__':
    unittest.main(verbosity=2)
