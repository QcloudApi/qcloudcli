# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeVpcTaskResultRequest(Request):

    def __init__(self):
        super(DescribeVpcTaskResultRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeVpcTaskResult', 'vpc.api.qcloud.com')

    def get_taskId(self):
        return self.get_params().get('taskId')

    def set_taskId(self, taskId):
        self.add_param('taskId', taskId)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
