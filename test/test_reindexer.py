# Copyright 2021 DCS Corporation, All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# DISTRIBUTION A. Approved for public release; distribution unlimited.
# OPSEC #4584.
#
# Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS
# Part 252.227-7013 or 7014 (Feb 2014).
#
# This notice must appear in all copies of this file and its derivatives.

import os
from pathlib import Path

from common import get_rosbag_options

import pytest

import rosbag2_py
from rosbag2_test_common import TESTED_STORAGE_IDS


RESOURCES_PATH = Path(os.environ['ROSBAG2_PY_TEST_RESOURCES_DIR'])


@pytest.mark.parametrize('storage_id', TESTED_STORAGE_IDS)
def test_reindexer_multiple_files(storage_id):
    bag_path = RESOURCES_PATH / storage_id / 'reindex_test_bags' / 'multiple_files'
    result_path = bag_path / 'metadata.yaml'

    storage_options, _ = get_rosbag_options(str(bag_path), storage_id=storage_id)
    reindexer = rosbag2_py.Reindexer()
    reindexer.reindex(storage_options)

    assert(result_path.exists())

    try:
        result_path.unlink()
    except FileNotFoundError:
        pass
