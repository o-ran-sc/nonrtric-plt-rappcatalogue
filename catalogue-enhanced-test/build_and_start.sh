#!/bin/bash

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

# Script to build and start the rapp catalogue enhanced container
# Make sure to run container including args as is this script

print_usage() {
    echo "Usage: ./build_and_start.sh"
    exit 1
}

if [ $# -ge 1 ]; then
    print_usage
fi

echo "Building rapp catalogue image..."
cd ../catalogue-enhanced/

#Build the image
docker build -t rapp_catalogue_enhanced_image .

docker stop rappcatalogueenhanced > /dev/null 2>&1
docker rm -f rappcatalogueenhanced > /dev/null 2>&1

echo "Starting rapp catalogue enhanced..."
echo "PWD path: "$PWD

#Run the container in interactive mode with host networking driver which allows docker to access localhost, unsecure port 9096, secure port 9196
docker run --network host --rm -it -p 9096:9096 -p 9196:9196 -e ALLOW_HTTP=true --volume "$PWD/certificate:/usr/src/app/cert" --name rappcatalogueenhanced rapp_catalogue_enhanced_image
