# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TerminateInstancesRequest(Request):

    def __init__(self):
        super(TerminateInstancesRequest, self).__init__(
            'cvm', 'qcloudcliV1', 'TerminateInstances', 'cvm.api.qcloud.com')

    def get_InstanceIds(self):
        return self.get_params().get('InstanceIds')

    def set_InstanceIds(self, InstanceIds):
        self.add_param('InstanceIds', InstanceIds)
