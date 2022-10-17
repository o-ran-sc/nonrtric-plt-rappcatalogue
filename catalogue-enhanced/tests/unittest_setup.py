#  ============LICENSE_START===============================================
#  Copyright (C) 2022 Nordix Foundation. All rights reserved.
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

# Setting up dir and env for unit test of rappcatalogueenhanced
import sys
import os
import pytest

#Server port and base path
PORT_NUMBER="9096"
HOST_IP="localhost"
SERVER_URL="http://"+HOST_IP+":"+PORT_NUMBER+"/"

#Dir for json test data files
testdata=""

def setup_env():
  global testdata
  cwd=os.getcwd()+"/"

  if 'TESTS_BASE_PATH' in os.environ:
    cwd = os.environ['TESTS_BASE_PATH']+"/"

  testdata = cwd+"../../catalogue-enhanced-test/jsonfiles/"

  #Env var to setup version and host logging
  os.environ['APIPATH'] = cwd+"../api/"
  os.environ['REMOTE_HOSTS_LOGGING'] = "ON"

  sys.path.append(os.path.abspath(cwd+'../src'))  # include: src
  sys.path.append(os.path.abspath(cwd+'../../catalogue-enhanced-test/common'))    # include: commons

  os.chdir(cwd+"../src")

def get_testdata_dir():
  return testdata

#Test client for rest calls
@pytest.fixture
def client():
  from main import app
  with app.app.test_client() as c:
    yield c
