# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TerminateComputeNodeRequest(Request):

    def __init__(self):
        super(TerminateComputeNodeRequest, self).__init__(
            'batch', 'qcloudcliV1', 'TerminateComputeNode', 'batch.api.qcloud.com')

    def get_ComputeNodeId(self):
        return self.get_params().get('ComputeNodeId')

    def set_ComputeNodeId(self, ComputeNodeId):
        self.add_param('ComputeNodeId', ComputeNodeId)

    def get_EnvId(self):
        return self.get_params().get('EnvId')

    def set_EnvId(self, EnvId):
        self.add_param('EnvId', EnvId)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
