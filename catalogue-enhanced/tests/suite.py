#  ============LICENSE_START===============================================
#  Copyright (C) 2023 Nordix Foundation. All rights reserved.
#  ========================================================================
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  ============LICENSE_END=================================================
#

# Combining all unit tests in one place

import os
import sys
import unittest

# Includes project source files
def setup_env():
  cwd=os.getcwd()+"/"
  sys.path.append(os.path.abspath(cwd+'../src'))

# Returns unit test cases from test modules
def suite():
  setup_env()
  suite= unittest.TestSuite()

  modules_to_test= []
  files= os.listdir('.')
  for afile in files:
    if afile.startswith('test') and afile.endswith('.py') and afile!= 'test_catalogue_enhanced.py':
      modules_to_test.append(afile.replace('.py', ''))

  for module in map(__import__, modules_to_test):
    tests= unittest.findTestCases(module)
    for test in tests:
      suite.addTest(test)

  return suite

if __name__ == '__main__':
  runner= unittest.TextTestRunner()
  runner.run(suite())
