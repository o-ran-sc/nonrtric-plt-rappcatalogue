## License

Copyright (C) 2022 Nordix Foundation.
Licensed under the Apache License, Version 2.0 (the "License")
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# O-RAN-SC Non-RT RIC rAPP Catalogue Enhanced

The O-RAN Non-RT RIC rApp Catalogue Enhanced provides an OpenApi 3.0 REST API for services to register/unregister themselves and discover other services.

The O-RAN Non-RT RIC rApp Catalogue Enhanced module supports GET, PUT and DELETE operations (version of the OpenAPI yaml file):

| Yaml file                    |     Version         |
| -----------------------------|-------------------- |
| rapp-catalogue-enhanced.yaml |      1.0.0          |

The overall folder structure is (relative to the location of this README file):

| Dir              | Description |
| ---------------- | ----------- |
|.                 |Dockerfile and README.md |
|api               |The OpenApi yaml |
|src               |Python source code |
|certificate       |A self-signed certificate and a key |

The application is being implemented in Python programming language.

The rApp Catalogue Enhanced module handles the requests that are defined in the OpenAPI yaml file. All these requests are implemented in the catalogue_manager.py module in the src folder. In addition, a number of utility functions are also supported and implemented by the main.py and payload_logging.py in the source folder.

The section below outlines the supported open api rest-based operations as well as the utility operations.

# Ports and certificates

The rApp Catalogue Enhanced module normally opens the port 9096 for http. If a certificate and a key are provided the module will open port 9196 for https instead. The port 9196 is only opened if a valid certificate and key is found.
The certificate and key shall be placed in the same directory and the directory shall be mounted to /usr/src/app/cert in the container.

| Port     | Protocol |
| -------- | ----- |
| 9096     | http  |
| 9196     | https |

The directory certificate contains a self-signed cert. Use the script generate_cert_and_key.sh to generate a new certificate and key. The password of the certificate must be set 'test'.
The same urls are availables on both the http port 9096 and the https port 9196. If using curl and https, the flag -k shall be given to make curl ignore checking the certificate.

# Supported operations in Non-RT RIC rAPP Catalogue Enhanced

For the complete yaml specification, see [OpenAPI.yaml](../api/rapp-catalogue-enhanced.yaml)

URIs for server:

| Function              | Path and parameters |
| --------------------- | ------------------- |
|  GET, Query all rapp ids | localhost:9096/rappcatalogue |
|  GET, Query rapp by rapp id | localhost:9096/rappcatalogue/<rapp_id> |
|  GET, Query API list by rapp id and service type | localhost:9096/rappcatalogue/<rapp_id>/<service_type> |
|  GET, Validate and query TOSCA.meta file content by rapp id | localhost:9096/rappcatalogue/csar/<rapp_id>/toscameta |
|  PUT, Register rapp | localhost:9096/rappcatalogue/<rapp_id> |
|  DELETE, Unregister rapp | localhost:9096/rappcatalogue/<rapp_id> |


# Admin functions

| Function              | Path and parameters |
| --------------------- | ------------------- |
|  POST, Delete all existing rapp definitions | localhost:9096/deleteall |


# Start and test of the Non-RT RIC rAPP Catalogue Enhanced

First, download the plt/rappcatalogue repo on gerrit:
git clone "https://gerrit.o-ran-sc.org/r/a/nonrtric/plt/rappcatalogue"

Goto the main directory, 'rappcatalogue/catalogue-enhanced-test'.
This folder contains a script to build and start the rAPP Catalogue Enhanced (as a container in interactive mode), a script for basic testing as well as json files for the test script.

Note that test can be performed both using the nonsecure http port and the secure https port.

Build and start the rApp catalogue enhanced containers:

./build_and_start.sh

This will build and start the container in interactive mode. The built container only resides in the local docker repository.
Note, the default port is 9096 for http and 9196 for https. When running the rapp catalogue enhanced as a container, the defualt ports can be re-mapped to any port on the localhost.

In a second terminal, go to the same folder and run the basic test script, basic_test.sh nonsecure|secure.

This script runs a number of tests towards the rapp catalogue enhanced to make sure it works properply.
