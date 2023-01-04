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

class SychronizedRappRegistry:

  def __init__(self):
    self.lock= RLock()
    self._rapps= {}

  def set_rapp(self, rapp_id, data):
    # Lock retry with fixed time-out (1 second)
    # Loop until lock acquired and task completed
    while True:
      if self.lock.acquire(blocking=False):
        print('Acquired a lock in set_rapp for the rapp: ', rapp_id)
        try:
          if rapp_id in self._rapps.keys():
            self._rapps[rapp_id]= data
            return 200
          else:
            self._rapps[rapp_id]= data
            return 201
        finally:
          self.lock.release()
          print('Released a lock in set_rapp for the rapp: ', rapp_id)
        break
      else:
        print('Waiting for a lock in set_rapp for the rapp: ', rapp_id)
        time.sleep(1.0)

  def del_rapp(self, rapp_id):
    while True:
      if self.lock.acquire(blocking=False):
        print('Acquired a lock in del_rapp for the rapp: ', rapp_id)
        try:
          if rapp_id in self._rapps.keys():
            del self._rapps[rapp_id]
            return rapp_id
        finally:
          self.lock.release()
          print('Released a lock in del_rapp for the rapp: ', rapp_id)
        break
      else:
        print('Waiting for a lock in del_rapp for the rapp: ', rapp_id)
        time.sleep(1.0)

  def get_rapp(self, rapp_id):
    while True:
      if self.lock.acquire(blocking=False):
        print('Acquired a lock in get_rapp for the rapp: ', rapp_id)
        try:
          if rapp_id in self._rapps.keys():
            return self._rapps[rapp_id]
        finally:
          self.lock.release()
          print('Released a lock in get_rapp for the rapp: ', rapp_id)
        break
      else:
        print('Waiting for a lock in get_rapp for the rapp: ', rapp_id)
        time.sleep(1.0)

  def clear_rapps(self):
    while True:
      if self.lock.acquire(blocking=False):
        print('Acquired a lock in clear_rapps')
        try:
          if self._rapps.keys():
            self._rapps.clear()
        finally:
          self.lock.release()
          print('Released a lock in clear_rapps')
        break
      else:
        print('Waiting for a lock in clear_rapps')
        time.sleep(1.0)

  def get_rapps_keys(self):
    while True:
      if self.lock.acquire(blocking=False):
        print('Acquired a lock in get_rapps_keys')
        try:
          return self._rapps.keys()
        finally:
          self.lock.release()
          print('Released a lock in get_rapps_keys')
        break
      else:
        print('Waiting for a lock in get_rapps_keys')
        time.sleep(1.0)
