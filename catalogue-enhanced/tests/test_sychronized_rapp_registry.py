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

from threading import Thread
from repository.synchronized_rapp_registry import SychronizedRappRegistry

class TestSynchronizedRappRegistry(unittest.TestCase):
  """
  Unit tests for SychronizedRappRegistry.py
  """

  def setUp(self):
    """setUp() runs before each test cases"""
    self.synch_registry = SychronizedRappRegistry()
    for i in range(0, 100):
      # add to the dict
      self.synch_registry.set_rapp(i, 'rapp'+str(i))

  def test_synch_registry_setup_size(self):
    self.assertEqual(100, len(self.synch_registry._rapps))

  def test_synch_registry_delete(self):
    for i in range(0, 100):
      # Create three threads for each element in the base dict, and try concurrent delete
      threads = [Thread(target=self.synch_registry.del_rapp(i)) for _ in range(3)]
      # start threads
      for thread in threads:
        thread.start()
      # wait for threads to finish
      for thread in threads:
        thread.join()
    self.assertEqual(0, len(self.synch_registry._rapps))

  def test_synch_registry_set(self):
    for i in range(0, 100):
      # Create three threads for each element in the base dict, and try concurrent set
      threads = [Thread(target=self.synch_registry.set_rapp(i, 'rapp'+str(i))) for _ in range(3)]
      # start threads
      for thread in threads:
        thread.start()
      # wait for threads to finish
      for thread in threads:
        thread.join()
    # The size of base dict should stay same
    self.assertEqual(100, len(self.synch_registry._rapps))
    self.assertEqual('rapp1', self.synch_registry.get_rapp(1))
    self.assertEqual('rapp99', self.synch_registry.get_rapp(99))

  def test_synch_registry_clear(self):
    # Create three threads for clear_base
    threads = [Thread(target=self.synch_registry.clear_rapps()) for _ in range(3)]
    # start threads
    for thread in threads:
      thread.start()
    # wait for threads to finish
    for thread in threads:
      thread.join()
    # The size of base dict should be zero
    self.assertEqual(0, len(self.synch_registry._rapps))

if __name__ == '__main__':
    unittest.main()
