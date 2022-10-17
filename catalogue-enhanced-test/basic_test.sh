#!/bin/bash

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

# Script for basic test of the rapp catalogue enhanced container
# Run the basic_test with either nonsecure or secure parameter

print_usage() {
    echo "Usage: ./basic_test.sh nonsecure|secure "
    exit 1
}

if [ $# -ne 1 ]; then
    print_usage
fi
if [ "$1" != "nonsecure" ] && [ "$1" != "secure" ]; then
    print_usage
fi

if [ $1 == "nonsecure" ]; then
    #Default http port for the rapp catalogue enhanced
    PORT=9096
    # Set http protocol
    HTTPX="http"
else
    #Default https port for the rapp catalogue enhanced
    PORT=9196
    # Set https protocol
    HTTPX="https"
fi

. ./common/test_common.sh

echo "=== Rapp catalogue enhanced health check ==="
RESULT="OK"
do_curl GET '/' 200

echo "=== Reset rapp catalogue enhanced ==="
RESULT="All rapp definitions deleted"
do_curl POST '/deleteall' 200

echo "=== API: Query all rapp ids, shall be empty array ==="
RESULT="json:[]"
do_curl GET '/rappcatalogue' 200

echo "=== API: Query rapp by rapp id , rapp rapp1 not found ==="
RESULT="json:{\"title\": \"The rapp does not exist.\", \"status\": 404, \"instance\": \"rapp1\"}"
do_curl GET '/rappcatalogue/rapp1' 404

echo "=== API: Register an rapp: rapp1 ==="
res=$(cat jsonfiles/rapp1.json)
RESULT="json:$res"
do_curl PUT  '/rappcatalogue/rapp1' 201 jsonfiles/rapp1.json

echo "=== API: Query all rapp ids, shall contain rapp id rapp1 ==="
RESULT="json:[ \"rapp1\" ]"
do_curl GET '/rappcatalogue' 200

echo "=== API: Query rapp by rapp id, rapp rapp1 found ==="
res=$(cat jsonfiles/rapp1.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp1' 200

echo "=== API: Filter api list by service type and rapp id, service type provider ==="
res=$(cat jsonfiles/rapp1_provider_apilist.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp1/provider' 200

echo "=== API: Filter api list by service type and rapp id, service type invoker ==="
res=$(cat jsonfiles/rapp1_invoker_apilist.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp1/invoker' 200

echo "=== API: Delete rapp by rapp id, rapp rapp1 deleted successfully ==="
RESULT=""
do_curl DELETE '/rappcatalogue/rapp1' 204

echo "=== API: Query all rapp ids, shall be empty array ==="
RESULT="json:[]"
do_curl GET '/rappcatalogue' 200

echo "=== API: Query rapp by rapp id , rapp rapp1 not found ==="
RESULT="json:{\"title\": \"The rapp does not exist.\", \"status\": 404, \"instance\": \"rapp1\"}"
do_curl GET '/rappcatalogue/rapp1' 404

echo "=== API: Register an rapp: rapp1 ==="
res=$(cat jsonfiles/rapp1.json)
RESULT="json:$res"
do_curl PUT  '/rappcatalogue/rapp1' 201 jsonfiles/rapp1.json

echo "=== API: Query all rapp ids, shall contain rapp id rapp1 ==="
RESULT="json:[ \"rapp1\" ]"
do_curl GET '/rappcatalogue' 200

echo "=== API: Query rapp by rapp id, rapp rapp1 found ==="
res=$(cat jsonfiles/rapp1.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp1' 200

echo "=== API: Query TOSCA.meta file by rapp_id, TOSCA.meta verified and listed ==="
res=$(cat jsonfiles/tosca_meta.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/csar/rapp1/toscameta' 200

echo "=== API: Query TOSCA.meta file by rapp_id, rapp does not exist ==="
RESULT="json:{\"title\": \"The rapp does not exist.\", \"status\": 404, \"instance\": \"rapp2\"}"
do_curl GET '/rappcatalogue/csar/rapp2/toscameta' 404

echo "=== API: Update an rapp: rapp1 ==="
res=$(cat jsonfiles/rapp1.json)
RESULT="json:$res"
do_curl PUT  '/rappcatalogue/rapp1' 200 jsonfiles/rapp1.json

echo "=== API: Query rapp by rapp id, rapp rapp1 found ==="
res=$(cat jsonfiles/rapp1.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp1' 200

echo "=== API: Register an rapp: rapp2 ==="
res=$(cat jsonfiles/rapp2.json)
RESULT="json:$res"
do_curl PUT  '/rappcatalogue/rapp2' 201 jsonfiles/rapp2.json

echo "=== API: Query rapp by rapp id, rapp rapp2 found ==="
res=$(cat jsonfiles/rapp2.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp2' 200

echo "=== API: Filter api list by service type and rapp id, service type provider ==="
res=$(cat jsonfiles/rapp2_provider_apilist.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp2/provider' 200

echo "=== API: Filter api list by service type and rapp id, service type invoker ==="
res=$(cat jsonfiles/rapp2_invoker_apilist.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp2/invoker' 200

echo "=== API: Query all rapp ids, shall contain rapp id rapp1 and rapp2 ==="
RESULT="json:[ \"rapp1\", \"rapp2\" ]"
do_curl GET '/rappcatalogue' 200

echo "=== API: Delete rapp by rapp id, rapp rapp1 deleted successfully ==="
RESULT=""
do_curl DELETE '/rappcatalogue/rapp1' 204

echo "=== API: Query rapp by rapp id , rapp rapp1 not found ==="
RESULT="json:{\"title\": \"The rapp does not exist.\", \"status\": 404, \"instance\": \"rapp1\"}"
do_curl GET '/rappcatalogue/rapp1' 404

echo "=== API: Query all rapp ids, shall contain rapp id rapp1 and rapp2 ==="
RESULT="json:[ \"rapp2\" ]"
do_curl GET '/rappcatalogue' 200

echo "=== API: Query rapp by rapp id, rapp rapp2 found ==="
res=$(cat jsonfiles/rapp2.json)
RESULT="json:$res"
do_curl GET '/rappcatalogue/rapp2' 200

echo "********************"
echo "*** All tests ok ***"
echo "********************"
