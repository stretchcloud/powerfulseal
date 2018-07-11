
# Copyright 2018 Bloomberg Finance L.P.
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


from powerfulseal.metriccollectors.collector import AbstractCollector


class StdoutCollector(AbstractCollector):
    """
        Passes metrics collected directly to stdout
    """

    def add_pod_killed_metric(self, node):
        print("Pod killed ")

    def add_pod_kill_failed_metric(self, node):
        print("Pod kill failed ")

    def add_node_stopped_metric(self, node):
        print("Node stopped ")

    def add_node_stop_failed_metric(self, node):
        print("Node stop failed ")

    def add_action_failed_metric(self):
        print("Action failed ")

    def add_filtered_to_empty_set_metric(self):
        print("Filtered to empty set ")

    def add_filtered_to_insufficient_random_sample_metric(self, sample_size, criterion):
        print("Filter (random sample) selected too few pods ")

    def add_filtering_passed_all_nodes_metric(self):
        print("Filtering passed all nodes ")

    def add_matched_to_empty_set_metric(self):
        print("Matched to empty set ")
