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

from repository.tosca_meta import ToscaMeta

class TestToscaMeta(unittest.TestCase):

  """
  Unit tests for ToscaMeta class
  """

  def test_toscameta_throws_exception_due_invalid_file_tag(self):
    with self.assertRaises(ValueError) as ve:
      ToscaMeta('TOSCA-Meta-File-Versio', 'CSAR-Version', 'Created-By')

    self.assertEqual(str(ve.exception), 'File tag should be like TOSCA-Meta-File-Version.')

  def test_toscameta_throws_exception_due_invalid_csar_tag(self):
    with self.assertRaises(ValueError) as ve:
      ToscaMeta('TOSCA-Meta-File-Version', 'CSAR-ersion', 'Created-By')

    self.assertEqual(str(ve.exception), 'CSAR tag should be like CSAR-Version.')

  def test_toscameta_throws_exception_due_invalid_createdby_tag(self):
    with self.assertRaises(ValueError) as ve:
      ToscaMeta('TOSCA-Meta-File-Version', 'CSAR-Version', 'CreatedBy')

    self.assertEqual(str(ve.exception), 'Created tag should like Created-By.')

if __name__ == '__main__':
    unittest.main()
