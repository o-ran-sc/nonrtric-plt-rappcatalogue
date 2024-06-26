#  ============LICENSE_START===============================================
#  Copyright (C) 2020-2022 Nordix Foundation. All rights reserved.
#  Copyright (C) 2024 OpenInfra Foundation Europe. All rights reserved.
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

from docs_conf.conf import *

#branch configuration

branch = 'latest'

language = 'en'

linkcheck_ignore = [
    'http://localhost.*',
    'http://127.0.0.1.*',
    'https://gerrit.o-ran-sc.org.*',
    './rac-api.html', #Generated file that doesn't exist at link check.
]

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.redoc',
]

redoc = [
            {
                'name': 'RAC API',
                'page': 'rac-api',
                'spec': '../api/rac-api.json',
                'embed': True,
            }
        ]

redoc_uri = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'

#intershpinx mapping with other projects
intersphinx_mapping = {}

intersphinx_mapping['nonrtric'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-nonrtric/en/%s' % branch, None)
