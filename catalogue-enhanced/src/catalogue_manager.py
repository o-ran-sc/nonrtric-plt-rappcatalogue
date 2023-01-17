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

import os
import json

from flask import request, Response
from jsonschema import validate
from var_declaration import synchronized_rapp_registry
from zipfile import ZipFile
from io import TextIOWrapper
from repository.tosca_meta import ToscaMeta

# Constsants
APPL_JSON='application/json'
TEXT_PLAIN='text/plain'
APPL_PROB_JSON='application/problem+json'

# API Function: Query for all rapp identifiers
def query_all_rapp_ids():

  allkeys= synchronized_rapp_registry.get_rapps_keys()
  res= list(allkeys)
  return (res, 200)


# API Function: Get a rapp definition
def query_rapp_by_id(rappid):

  rapp_id= str(rappid)
  rapp_definition= synchronized_rapp_registry.get_rapp(rapp_id)

  if rapp_definition:
    return Response(json.dumps(rapp_definition), 200, mimetype=APPL_JSON)
  else:
    pjson=create_problem_json(None, "The rapp does not exist.", 404, None, rapp_id)
    return Response(json.dumps(pjson), 404, mimetype=APPL_PROB_JSON)


# API Function: Register, or update, a rapp definition
def register_rapp(rappid):

  rapp_id=str(rappid)

  try:
    data = request.data
    data = json.loads(data)
  except Exception:
    pjson=create_problem_json(None, "The rapp definition is corrupt or missing.", 400, None, rapp_id)
    return Response(json.dumps(pjson), 400, mimetype=APPL_PROB_JSON)

  response_code= synchronized_rapp_registry.set_rapp(rapp_id, data)
  return Response(json.dumps(data), response_code, mimetype=APPL_JSON)


# API Function: Unregister a rapp from catalogue
def unregister_rapp(rappid):

  rapp_id = str(rappid)

  if synchronized_rapp_registry.del_rapp(rapp_id):
    return Response('', 204, mimetype=APPL_JSON)
  else:
    pjson = create_problem_json(None, "The rapp definition does not exist.", 404, None, rapp_id)
    return Response(json.dumps(pjson), 404, mimetype=APPL_PROB_JSON)


# API Function: Query api list by rapp_id and service_type: produced or consumed
def query_api_list_by_rapp_id_and_service_type(rappid, servicetype):

  rapp_id = str(rappid)
  service_type = str(servicetype)

  rapp_definition= synchronized_rapp_registry.get_rapp(rapp_id)

  if rapp_definition:
    try:
      arr_api_list = rapp_definition['apiList']
      arr_filtered_api_list = [arr_item for arr_item in arr_api_list if arr_item['serviceType'] == service_type]
      return (arr_filtered_api_list, 200)
    except Exception as err:
      print('An error occured:', err)
      pjson=create_problem_json(None, "The rapp definition is corrupt or missing.", 400, None, rapp_id)
      return Response(json.dumps(pjson), 400, mimetype=APPL_PROB_JSON)

  return ([], 200)


# API Function: Validate and return TOSCA.meta file content
def query_tosca_meta_content_by_rapp_id(rappid):

  rapp_id = str(rappid)

  if synchronized_rapp_registry.get_rapp(rapp_id):
    with open_zip_and_filter('/usr/src/app/csar/rapp1/rapp1.csar') as tosca_file:
      tosca_meta = []
      while True:
        line = tosca_file.readline()  # Get next line from file
        if not line:  # end of file is reached
          break
        else:
          tosca_meta.append(line.strip())

    try:
      validate_tosca_meta_format(tosca_meta)
      return Response(json.dumps(tosca_meta), 200, mimetype=APPL_JSON)
    except Exception as err:
      print('An error occured:', err)
      pjson=create_problem_json(None, err, 512, None, rapp_id)
      return Response(json.dumps(pjson), 512, mimetype=APPL_PROB_JSON)

  else:
    pjson=create_problem_json(None, "The rapp does not exist.", 404, None, rapp_id)
    return Response(json.dumps(pjson), 404, mimetype=APPL_PROB_JSON)


# Helper: Open CSAR zip file and returns TOSCA.meta
def validate_tosca_meta_format(toscameta):

  if len(toscameta) >= 3:
    file_tag = split_and_strip(toscameta[0])
    csar_tag = split_and_strip(toscameta[1])
    crby_tag = split_and_strip(toscameta[2])

    ToscaMeta(file_tag, csar_tag, crby_tag)
  else:
    raise ValueError("More lines than expected in Tosca.meta")

# Helper: Splits given string by colon and strip
def split_and_strip(string):
  result = [x.strip() for x in string.split(':')]
  return result[0]

# Helper: Open CSAR zip file and returns TOSCA.meta file
def open_zip_and_filter(filename):

  try:
    with ZipFile(filename, 'r') as zip_object:
      file_names = zip_object.namelist()
      for file_name in file_names:
        if file_name.endswith('TOSCA.meta'):
          return TextIOWrapper(zip_object.open(file_name))  # TextIOWrapper: provides buffered text stream
  except Exception as err:
    pjson=create_problem_json(None, "The CSAR zip content is corrupt or missing.", 400, None, rapp_id)
    return Response(json.dumps(pjson), 400, mimetype=APPL_PROB_JSON)
  finally:
    zip_object.close()

# Helper: Create a problem json object
def create_problem_json(type_of, title, status, detail, instance):

  error = {}
  if type_of is not None:
    error["type"] = type_of
  if title is not None:
    error["title"] = title
  if status is not None:
    error["status"] = status
  if detail is not None:
    error["detail"] = detail
  if instance is not None:
    error["instance"] = instance
  return error


# Helper: Create a problem json based on a generic http response code
def create_error_response(code):

    if code == 400:
      return(create_problem_json(None, "Bad request", 400, "Object in payload not properly formulated or not related to the method", None))
    elif code == 404:
      return(create_problem_json(None, "Not found", 404, "No resource found at the URI", None))
    elif code == 405:
      return(create_problem_json(None, "Method not allowed", 405, "Method not allowed for the URI", None))
    elif code == 408:
      return(create_problem_json(None, "Request timeout", 408, "Request timeout", None))
    elif code == 409:
      return(create_problem_json(None, "Conflict", 409, "Request could not be processed in the current state of the resource", None))
    elif code == 429:
      return(create_problem_json(None, "Too many requests", 429, "Too many requests have been sent in a given amount of time", None))
    elif code == 503:
      return(create_problem_json(None, "Service unavailable", 503, "The provider is currently unable to handle the request due to a temporary overload", None))
    elif code == 507:
      return(create_problem_json(None, "Insufficient storage", 507, "The method could not be performed on the resource because the provider is unable to store the representation needed to successfully complete the request", None))
    elif code == 512:
      return(create_problem_json(None, "Tosca.meta not valid", 512, "TOSCA.meta content is not valid", None))
    else:
      return(create_problem_json(None, "Unknown", code, "Not implemented response code", None))
