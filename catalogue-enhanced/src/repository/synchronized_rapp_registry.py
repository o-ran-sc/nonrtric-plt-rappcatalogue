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

from threading import RLock
import time
import logging

from maincommon import active_logger_profile

log= logging.getLogger(active_logger_profile)

class SychronizedRappRegistry:

  def __init__(self):
    self.lock= RLock()
    self._rapps= {}

  def set_rapp(self, rapp_id, data):
    with self.lock:
      log.debug('Acquired a lock in set_rapp for the rapp: %s', rapp_id)
      if rapp_id in self._rapps.keys():
        self._rapps[rapp_id]= data
        return 200
      else:
        self._rapps[rapp_id]= data
        return 201

  def del_rapp(self, rapp_id):
    with self.lock:
      log.debug('Acquired a lock in del_rapp for the rapp: %s', rapp_id)
      if rapp_id in self._rapps.keys():
        del self._rapps[rapp_id]
        return rapp_id

  def get_rapp(self, rapp_id):
    with self.lock:
      log.debug('Acquired a lock in get_rapp for the rapp: %s', rapp_id)
      if rapp_id in self._rapps.keys():
        return self._rapps[rapp_id]

  def clear_rapps(self):
    with self.lock:
      log.debug('Acquired a lock in clear_rapps')
      if self._rapps.keys():
        self._rapps.clear()

  def get_rapps_keys(self):
    with self.lock:
      log.debug('Acquired a lock in get_rapps_keys')
      return self._rapps.keys()
