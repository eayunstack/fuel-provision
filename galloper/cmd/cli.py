# Copyright 2013: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys
from oslo.config import cfg

from galloper.cli.parser import GalloperCli
from galloper.openstack.common import log as logging


CONF = cfg.CONF


def run():
    logging.setup("galloper-cli")

    try:
        GalloperCli().main(sys.argv[1:])
    except Exception as e:
        print("Error occured while running CLI.")
        print(str(e.message))
        sys.exit(1)

