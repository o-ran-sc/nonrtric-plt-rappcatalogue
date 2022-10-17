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

class ToscametaFormatChecker:
  """
  A utility class aims to check required fields and their format
  in TOSCA.meta file in accordance with TOSCA specs.
  """
  def __init__(self, file_ver, csar_ver, created_by):
    self.file_ver = file_ver
    self.csar_ver = csar_ver
    self.created_by = created_by

  def validate(self):

    if (self.file_ver == 'TOSCA-Meta-File-Version' and
        self.csar_ver == 'CSAR-Version' and
        self.created_by == 'Created-By'):

      return True
    else:
      return False

  def __str__(self):  # __str__: returns display string
    return '[TOSCA.meta: %s, %s, %s]' % (self.file_ver, self.csar_ver, self.created_by)

# Unit tests for class: ToscametaFormatChecker
if __name__ == '__main__':
  toscameta_t = ToscametaFormatChecker('TOSCA-Meta-File-Version', 'CSAR-Version', 'Created-By')
  assert toscameta_t.validate() is True

  toscameta_f = ToscametaFormatChecker('TOSCA-Meta-File-Versn', 'CSAR-Version', 'Created-By')
  assert toscameta_f.validate() is False
