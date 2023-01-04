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

from threading import RLock
from maincommon import apipath
import connexion

class SychronizedRappRegistry:

  def __init__(self):
    self.lock= RLock()
    self.base= {}

  def set_rapp(self, rapp_id, data):
    self.lock.acquire()
    try:
      self.base[rapp_id]= data
    except Exception as err:
      print('An error occured while set rapp:', err)
    finally:
      self.lock.release()

  def del_rapp(self, rapp_id):
    self.lock.acquire()
    try:
      del self.base[rapp_id]
    except Exception as err:
      print('An error occured while del rapp:', err)
    finally:
      self.lock.release()

  def get_rapp(self, rapp_id):
    self.lock.acquire()
    try:
      return self.base[rapp_id]
    except Exception as err:
      print('An error occured while get rapp:', err)
    finally:
      self.lock.release()

  def clear_base(self):
    self.lock.acquire()
    try:
      self.base.clear()
    except Exception as err:
      print('An error occured while get rapp:', err)
    finally:
      self.lock.release()

  def get_base_keys(self):
    self.lock.acquire()
    try:
      return self.base.keys()
    except Exception as err:
      print('An error occured while get rapp:', err)
    finally:
      self.lock.release()

synchronized_rapp_registry= SychronizedRappRegistry()
register_rapp_lock= RLock()
query_api_list_lock= RLock()

#Main app
app = connexion.App(__name__, specification_dir=apipath)

