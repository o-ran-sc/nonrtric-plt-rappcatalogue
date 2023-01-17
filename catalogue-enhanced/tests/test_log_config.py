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

import unittest
import logging
import logging.config
import os
import yaml

from configuration.log_config import Logger

LOG_CONFIG_PATH= '../config/logger.yaml'

class TestLogConfig(unittest.TestCase):
  """
  Unit tests for TestLogConfig class
  """

  def test_log_config_does_not_exist_then_use_root_logger(self):
    Logger()

    logger= logging.getLogger()
    self.assertEqual('root', logger.name)
    self.assertEqual(logging.WARNING, logger.level)

  def test_log_config_exist_then_logger_dev_exist(self):
    Logger(LOG_CONFIG_PATH)

    logger= logging.getLogger('dev')
    self.assertEqual('dev', logger.name)

  def test_log_config_exist_then_logger_dev_handlers_exist(self):
    Logger(LOG_CONFIG_PATH)

    logger= logging.getLogger('dev')
    handlers= [handler.name for handler in logger.handlers]

    self.assertEqual(['console', 'file'], handlers)

  def test_log_config_exist_then_check_logger_prod_exists(self):
    Logger(LOG_CONFIG_PATH)

    logger= logging.getLogger('prod')
    self.assertEqual('prod', logger.name)

  def test_log_config_exist_then_logger_prod_handlers_exist(self):
    Logger(LOG_CONFIG_PATH)

    logger= logging.getLogger('prod')
    handlers= [handler.name for handler in logger.handlers]

    self.assertEqual(['console'], handlers)

if __name__ == '__main__':
    unittest.main()

