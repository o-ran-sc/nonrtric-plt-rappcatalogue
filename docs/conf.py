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

#extensions = ['sphinxcontrib.redoc', 'sphinx.ext.intersphinx',]

extensions = [
   # ...
   #'sphinxcontrib.redoc',
   'sphinxcontrib.openapi',
   'sphinx.ext.intersphinx',
]

#redoc = [
            #{
                #'name': 'RAC API',
                #'page': 'rac-api',
                #'spec': '../api/rac-api.json',
                #'embed': True,
            #}
        #]

#redoc_uri = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'

#intershpinx mapping with other projects
intersphinx_mapping = {}

intersphinx_mapping['nonrtric'] = ('https://docs.o-ran-sc.org/projects/o-ran-sc-nonrtric/en/%s' % branch, None)
