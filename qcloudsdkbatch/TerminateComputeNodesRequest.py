# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TerminateComputeNodesRequest(Request):

    def __init__(self):
        super(TerminateComputeNodesRequest, self).__init__(
            'batch', 'qcloudcliV1', 'TerminateComputeNodes', 'batch.api.qcloud.com')

    def get_ComputeNodeIds(self):
        return self.get_params().get('ComputeNodeIds')

    def set_ComputeNodeIds(self, ComputeNodeIds):
        self.add_param('ComputeNodeIds', ComputeNodeIds)

    def get_EnvId(self):
        return self.get_params().get('EnvId')

    def set_EnvId(self, EnvId):
        self.add_param('EnvId', EnvId)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
