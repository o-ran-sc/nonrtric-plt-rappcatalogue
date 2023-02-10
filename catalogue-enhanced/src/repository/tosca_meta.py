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


class ToscaMeta:

  """
  A utility class aims to check required fields and their format
  in TOSCA.meta file in accordance with TOSCA specs.
  """

  TOSCA= 'TOSCA-Meta-File-Version'
  CSAR= 'CSAR-Version'
  CREATEDBY= 'Created-By'

  def __init__(self, file_tag, csar_tag, createdby_tag):
    self.file_tag = self.is_valid_file_tag(file_tag)
    self.csar_tag = self.is_valid_csar_tag(csar_tag)
    self.createdby_tag = self.is_valid_createdby_tag(createdby_tag)

  def is_valid_file_tag(self, file_tag):
    if file_tag!= ToscaMeta.TOSCA:
      raise ValueError("File tag should be like TOSCA-Meta-File-Version.")

    return file_tag

  def is_valid_csar_tag(self, csar_tag):
    if csar_tag!= ToscaMeta.CSAR:
      raise ValueError("CSAR tag should be like CSAR-Version.")

    return csar_tag

  def is_valid_createdby_tag(self, createdby_tag):
    if createdby_tag!= ToscaMeta.CREATEDBY:
      raise ValueError("Created tag should like Created-By.")

    return createdby_tag

  def __str__(self):  # __str__: returns display string
    return '[TOSCA.meta: %s, %s, %s]' % (self.file_tag, self.csar_tag, self.createdby_tag)
