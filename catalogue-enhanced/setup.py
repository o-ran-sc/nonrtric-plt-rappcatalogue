#!/usr/bin/env python

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

from setuptools import setup

setup(name='rappcatalogue-enhanced',
      version='1.1.0',
      description='The O-RAN Non-RT RIC rApp Catalogue Enhanced provides an OpenApi 3.0 REST API for rApp services to register/unregister themselves and discover other services',
      url='https://gerrit.o-ran-sc.org/r/admin/repos/nonrtric/plt/rappcatalogue,general',
      license='Apache License, Version 2.0',
      platforms='any',
      packages=[
          'src',
          'src.configuration',
          'src.repository',
          'api',
          'certificate',
          'config',
          'csar',
          'tests'
      ],
      zip_safe=False,
      include_package_data=True,
      install_requires=[
          'connexion[swagger-ui]',
      ],
)
