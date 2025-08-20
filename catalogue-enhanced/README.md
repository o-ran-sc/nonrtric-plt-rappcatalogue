## License

Copyright (C) 2022-2023 Nordix Foundation.
Copyright (C) 2023-2025 OpenInfra Foundation Europe.
Licensed under the Apache License, Version 2.0 (the "License")
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# O-RAN-SC Non-RT RIC rApp Catalogue Enhanced

![Status: Deprecated](https://img.shields.io/badge/status-deprecated-red)
![Status: Experimental](https://img.shields.io/badge/CVE%20Support-none-lightgrey)

> [!CAUTION]
> **Deprecated**
>
> This repository is no longer actively maintained or supported.
>
> Please refer to the [o-ran-sc/nonrtric-plt-rappmanager](https://github.com/o-ran-sc/nonrtric-plt-rappmanager) repository for the actively maintained rApp Manager and rApps.

The O-RAN Non-RT RIC rApp Catalogue Enhanced provides an OpenApi 3.0 REST API for services to register/unregister themselves and discover other services.

The O-RAN Non-RT RIC rApp Catalogue Enhanced module supports GET, PUT and DELETE operations. For the specifications please refer to [OpenAPI.yaml] ./api/rapp-catalogue-enhanced.yaml

|Yaml file                    |     Version         |
|-----------------------------|-------------------- |
|rapp-catalogue-enhanced.yaml |      1.2.0          |

The overall folder structure is (relative to the location of this README file):

| Dir              | Description |
| ---------------- | ----------- |
|.                 |Dockerfile, container-tag.yaml, nginx.conf, pyproject.toml, tox.ini, setup.py, and README.md |
|api               |The OpenApi yaml rapp-catalogue-enhanced.yaml |
|src               |Python source codes includes sub-directories repository, configuration, and start.sh |
|certificate       |A self-signed certificate and a key |
|config            |Configuration files such as logger.yaml |
|csar              |CSAR files such as csar/rapp1.csar |
|tests             |Python unit tests, Pytest fixture, and test setup utility |

The other folder structure (catalogue-enhanced-test) that includes tests implemented in bash via Curl:

| Dir              | Description |
| ---------------- | ----------- |
|.                 |build_and_start.sh, and basic_test.sh |
|common            |compare_json.py and test_commons.sh are the utilities to compare json files |
|jsonfiles         |JSON scripts related to API responses |

The application is being implemented in Python programming language.

The rApp Catalogue Enhanced module handles the requests that are defined in the OpenAPI YAML file. All these requests are implemented in the catalogue_manager.py module in the src folder. The CRUD operations of rApps have been implemented in synchronized blocks so that multi-thread access could not lead to inconsistency of the data. In addition, the logging functions are also supported and implemented by payload_logging.py and log_config.py in the configuration folder.

The section below outlines the supported OpenAPI rest-based operations as well as the utility operations.

# Ports and certificates

The rApp Catalogue Enhanced module normally opens the port 9096 for HTTP. If a certificate and a key are provided the module will open port 9196 for HTTPS instead. The port 9196 is only opened if a valid certificate and key is found. The certificate and key shall be placed in the same directory and the directory shall be mounted to /usr/src/app/cert in the container.

| Port     | Protocol |
| -------- | ----- |
| 9096     | http  |
| 9196     | https |

The directory certificate contains a self-signed cert. Use the script generate_cert_and_key.sh to generate a new certificate and key. The password of the certificate must be set 'test'. The same urls are availables on both the http port 9096 and the https port 9196. If using CURL and HTTPS, the flag -k shall be given to make curl ignore checking the certificate.

# Supported operations in Non-RT RIC rApp Catalogue Enhanced

For the complete YAML specification, see [OpenAPI.yaml](./api/rapp-catalogue-enhanced.yaml)

URIs for server:

| Function              | Path and parameters |
| --------------------- | ------------------- |
|GET, Query all rapp ids | localhost:9096/rappcatalogue |
|GET, Query rapp by rapp id | localhost:9096/rappcatalogue/<rapp_id> |
|GET, Query API list by rapp id and service type | localhost:9096/rappcatalogue/<rapp_id>/<service_type> |
|GET, Validate and query TOSCA.meta file content by rapp id | localhost:9096/rappcatalogue/csar/<rapp_id>/toscameta |
|PUT, Register rapp | localhost:9096/rappcatalogue/<rapp_id> |
|DELETE, Unregister rapp | localhost:9096/rappcatalogue/<rapp_id> |


# Admin functions

| Function              | Path and parameters |
| --------------------- | ------------------- |
|POST, Delete all existing rapp definitions | localhost:9096/deleteall |


# Start and test of the Non-RT RIC rAPP Catalogue Enhanced

First, download the plt/rappcatalogue repo on gerrit:

git clone "https://gerrit.o-ran-sc.org/r/a/nonrtric/plt/rappcatalogue"

Goto the main directory, 'rappcatalogue/catalogue-enhanced-test'. This folder contains a script to build and start the rApp Catalogue Enhanced (as a container in interactive mode), a script for basic testing as well as JSON files for the test script.

Note that test can be performed both using the nonsecure HTTP port and the secure HTTPS port.

# Building the rApp Catalogue Enhanced

Build and start the rApp catalogue enhanced containers:

./build_and_start.sh

This will build and start the container in interactive mode. The built container only resides in the local docker repository. When running the rApp Catalogue Enhanced as a container, the defualt ports can be re-mapped to any port on the localhost.

# API Testing of rApp Catalogue Enhanced

In a second terminal, go to the same folder and run the basic test script:
      basic_test.sh nonsecure|secure.

This script runs a number of API tests towards the rApp Catalogue Enhanced to make sure it works properply.

# Unit Testing of rApp Catalogue Enhanced

In order to run unit test cases, there is no need to build, and start any container. However, Python's venv must exist. You can follow the below steps to create a venv:
      1- Change current directory to project's root directory that is rappcatalogue.
      2- Run the commands consecutively:
            python3 -m venv venv --prompt="rappcatalogue"
            source venv/bin/activate
            pip install connexion
      3- Change current directory to 'catalogue-enhanced/tests/'
      4- Run the command below:
            python suite.py
The suite.py will detect existing unit test cases, and run them all.

# Installing the pip distribution of rApp Catalogue Enhanced

It is also possible to have a pip distro of rApp catalogue. In order to install in your venv, you have to first install a venv mentioned in Unit Testing of rApp.

Then, you can follow the below steps:
      1- Change current directory to 'rappcatalogue/catalogue-enhanced' where you can find setup.py
      2- Run the command:
            pip install .

This will build the rApp catalogue on your local.


