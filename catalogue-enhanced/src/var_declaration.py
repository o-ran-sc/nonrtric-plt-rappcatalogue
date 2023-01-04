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

from threading import RLock
from maincommon import apipath
from repository.synchronized_rapp_registry import SychronizedRappRegistry

import os
import sys
import connexion
import logging
import logging.config
import yaml

def init_logger():
  with open('/usr/src/app/config/logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


synchronized_rapp_registry= SychronizedRappRegistry()

#Main app
app = connexion.App(__name__, specification_dir=apipath)

