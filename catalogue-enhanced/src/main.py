#  ============LICENSE_START===============================================
#  Copyright (C) 2022-2023 Nordix Foundation. All rights reserved.
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

import sys

from flask import Response, Flask
from var_declaration import app, synchronized_rapp_registry
from configuration.log_config import Logger

# App var need to be initialized
import configuration.payload_logging

# Constants
TEXT_PLAIN='text/plain'
LOG_CONFIG_PATH= '/usr/src/app/config/logger.yaml'

# Check alive function
@app.route('/', methods=['GET'])
def test():
  return Response("OK", 200, mimetype=TEXT_PLAIN)

# Delete all rapp definitions
@app.route('/deleteall', methods=['POST'])
def delete_all():
  synchronized_rapp_registry.clear_rapps()

  return Response("All rapp definitions deleted", 200, mimetype=TEXT_PLAIN)

port_number = 9696
if len(sys.argv) >= 2 and isinstance(sys.argv[1], int):
    port_number = sys.argv[1]

# Import base RESTFul API functions from Open API
app.add_api('rapp-catalogue-enhanced.yaml')

if __name__ == '__main__':
  Logger(LOG_CONFIG_PATH)
  app.run(port=port_number, host="0.0.0.0", threaded=False)
