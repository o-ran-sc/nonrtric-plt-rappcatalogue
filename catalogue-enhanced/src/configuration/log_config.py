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

import logging
import logging.config
import os
import yaml

DEFAULT_LEVEL= logging.INFO

class Logger:

  def __init__(self, log_cfg_path= None):
    if log_cfg_path and os.path.exists(log_cfg_path):
      with open(log_cfg_path, 'r') as cfg_file:
        try:
          config = yaml.safe_load(cfg_file.read())
          logging.config.dictConfig(config)
        except Exception as e:
          print('Error with log-config file: ', e)
    else:
      print('No config file found,  using default logger')
