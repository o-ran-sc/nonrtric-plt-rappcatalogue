#
# ============LICENSE_START=======================================================
#  Copyright (C) 2020 Nordix Foundation.
# ================================================================================
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============LICENSE_END=========================================================
#
#Get JDK & shrink it to equivalent to a JRE
FROM openjdk:17-jdk as jre-build
RUN $JAVA_HOME/bin/jlink \
   --verbose \
   --add-modules ALL-MODULE-PATH \
   --strip-debug \
   --no-man-pages \
   --no-header-files \
   --compress=2 \
   --output /customjre

# Use debian base image (same as openjdk uses)
FROM debian:11-slim

#Copy JRE from the jre-base image
ENV JAVA_HOME=/jre
ENV PATH=${JAVA_HOME}/bin:${PATH}
COPY --from=jre-build /customjre $JAVA_HOME
ARG JAR

WORKDIR /opt/app/rappcatalogue
RUN mkdir -p /var/log/rappcatalogue
RUN mkdir -p /opt/app/rappcatalogue/etc/cert/

EXPOSE 8680 8633

ADD /config/application.yaml /opt/app/rappcatalogue/config/application.yaml
ADD /config/rappcatalogue-keystore.jks /opt/app/rappcatalogue/etc/cert/keystore.jks
ADD target/${JAR} /opt/app/rappcatalogue/rappcatalogue.jar

ARG user=nonrtric
ARG group=nonrtric

RUN groupadd $user && \
    useradd -r -g $group $user
RUN chown -R $user:$group /opt/app/rappcatalogue
RUN chown -R $user:$group /var/log/rappcatalogue

USER ${user}

CMD ["java", "-jar", "/opt/app/rappcatalogue/rappcatalogue.jar"]




