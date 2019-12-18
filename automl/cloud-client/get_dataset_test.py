# Copyright 2019 Google LLC
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

import os

import get_dataset

PROJECT_ID = os.environ["GCLOUD_PROJECT"]
DATASET_ID = "TEN4058147884539838464"


def test_get_dataset(capsys):
    get_dataset.get_dataset(PROJECT_ID, DATASET_ID)
    out, _ = capsys.readouterr()
    assert "Dataset name: " in out
