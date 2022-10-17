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

# This fixture tests the rappcatalogueenhanced module
import json
import time
from unittest_setup import SERVER_URL, setup_env, get_testdata_dir, client

#Setup env and import paths
setup_env()
from compare_json import compare

def test_apis(client):

  RESP_TITLE = "The rapp does not exist."
  RAPP1 = 'rappcatalogue/rapp1'
  RAPP2 = 'rappcatalogue/rapp2'
  RAPP1_JSON = 'rapp1.json'
  RAPP2_JSON = 'rapp2.json'

  testdata = get_testdata_dir()

  # Header for json payload
  header = {
    "Content-Type" : "application/json"
  }

  # rappcatalogueenhanced hello world
  response = client.get(SERVER_URL)
  assert response.status_code == 200

  # Reset rapp catalogue enhanced
  response = client.post(SERVER_URL+'deleteall')
  assert response.status_code == 200
  assert response.data ==  b"All rapp definitions deleted"

  # API: Query all rapp ids, shall be empty array
  data_response = [ ]
  response = client.get(SERVER_URL+'rappcatalogue')
  result = json.loads(response.data)
  res = compare(data_response, result)
  assert response.status_code == 200
  assert res == True

  # API: Query rapp by rapp id , rapp rapp1 not found
  data_response = {"title": RESP_TITLE, "status": 404, "instance": "rapp1"}
  response=client.get(SERVER_URL+RAPP1)
  result=json.loads(response.data)
  res=compare(data_response, result)
  assert response.status_code == 404
  assert res == True

  # API: Register an rapp: rapp1
  with open(testdata+RAPP1_JSON) as json_file:
    json_payload = json.loads(json_file.read())
    response = client.put(SERVER_URL+RAPP1, headers=header, data=json.dumps(json_payload))
    result = json.loads(response.data)
    res = compare(json_payload, result)
    assert response.status_code == 201
    assert res == True

  # API: Query all rapp ids, shall contain rapp id rapp1
  data_response = ['rapp1']
  response = client.get(SERVER_URL+'rappcatalogue')
  result = json.loads(response.data)
  res = compare(data_response, result)
  assert response.status_code == 200
  assert res == True

  # API: Query rapp by rapp id, rapp rapp1 found
  with open(testdata+RAPP1_JSON) as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+RAPP1)
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Filter api list by service type and rapp id, service type provider
  with open(testdata+'rapp1_provider_apilist.json') as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+'rappcatalogue/rapp1/provider')
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Filter api list by service type and rapp id, service type invoker
  with open(testdata+'rapp1_invoker_apilist.json') as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+'rappcatalogue/rapp1/invoker')
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Delete rapp by rapp id, rapp rapp1 deleted successfully
  data_response = b""
  response=client.delete(SERVER_URL+RAPP1)
  assert response.status_code == 204
  assert data_response == response.data

  # API: Query all rapp ids, shall be empty array
  data_response = [ ]
  response = client.get(SERVER_URL+'rappcatalogue')
  result = json.loads(response.data)
  res = compare(data_response, result)
  assert response.status_code == 200
  assert res == True

  # API: Query rapp by rapp id , rapp rapp1 not found
  data_response = {"title": RESP_TITLE, "status": 404, "instance": "rapp1"}
  response=client.get(SERVER_URL+RAPP1)
  result=json.loads(response.data)
  res=compare(data_response, result)
  assert response.status_code == 404
  assert res == True

  # API: Register an rapp: rapp1
  with open(testdata+RAPP1_JSON) as json_file:
    json_payload = json.loads(json_file.read())
    response = client.put(SERVER_URL+RAPP1, headers=header, data=json.dumps(json_payload))
    result = json.loads(response.data)
    res = compare(json_payload, result)
    assert response.status_code == 201
    assert res == True

  # API: Query all rapp ids, shall contain rapp id rapp1
  data_response = ['rapp1']
  response = client.get(SERVER_URL+'rappcatalogue')
  result = json.loads(response.data)
  res = compare(data_response, result)
  assert response.status_code == 200
  assert res == True

  # API: Query rapp by rapp id, rapp rapp1 found
  with open(testdata+RAPP1_JSON) as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+RAPP1)
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Update an rapp: rapp1
  with open(testdata+RAPP1_JSON) as json_file:
    json_payload = json.loads(json_file.read())
    response = client.put(SERVER_URL+RAPP1, headers=header, data=json.dumps(json_payload))
    result = json.loads(response.data)
    res = compare(json_payload, result)
    assert response.status_code == 200
    assert res == True

  # API: Query rapp by rapp id, rapp rapp1 found
  with open(testdata+RAPP1_JSON) as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+RAPP1)
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Register an rapp: rapp2
  with open(testdata+RAPP2_JSON) as json_file:
    json_payload = json.loads(json_file.read())
    response = client.put(SERVER_URL+RAPP2, headers=header, data=json.dumps(json_payload))
    result = json.loads(response.data)
    res = compare(json_payload, result)
    assert response.status_code == 201
    assert res == True

  # API: Query rapp by rapp id, rapp rapp2 found
  with open(testdata+RAPP2_JSON) as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+RAPP2)
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Filter api list by service type and rapp id, service type provider
  with open(testdata+'rapp2_provider_apilist.json') as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+'rappcatalogue/rapp2/provider')
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Filter api list by service type and rapp id, service type invoker
  with open(testdata+'rapp2_invoker_apilist.json') as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+'rappcatalogue/rapp2/invoker')
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True

  # API: Query all rapp ids, shall contain rapp id rapp1 and rapp2
  data_response = ['rapp1', 'rapp2']
  response = client.get(SERVER_URL+'rappcatalogue')
  result = json.loads(response.data)
  res = compare(data_response, result)
  assert response.status_code == 200
  assert res == True

  # API: Delete rapp by rapp id, rapp rapp1 deleted successfully
  data_response = b""
  response=client.delete(SERVER_URL+RAPP1)
  assert response.status_code == 204
  assert data_response == response.data

  # API: Query rapp by rapp id , rapp rapp1 not found
  data_response = {"title": RESP_TITLE, "status": 404, "instance": "rapp1"}
  response=client.get(SERVER_URL+RAPP1)
  result=json.loads(response.data)
  res=compare(data_response, result)
  assert response.status_code == 404
  assert res == True

  # API: Query all rapp ids, shall contain rapp id rapp2
  data_response = ['rapp2']
  response = client.get(SERVER_URL+'rappcatalogue')
  result = json.loads(response.data)
  res = compare(data_response, result)
  assert response.status_code == 200
  assert res == True

  # API: Query rapp by rapp id, rapp rapp2 found
  with open(testdata+RAPP2_JSON) as json_file:
    data_response = json.load(json_file)
    response = client.get(SERVER_URL+RAPP2)
    result = json.loads(response.data)
    res = compare(data_response, result)
    assert response.status_code == 200
    assert res == True
