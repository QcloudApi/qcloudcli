# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeTaskInfoRequest(Request):

    def __init__(self):
        super(DescribeTaskInfoRequest, self).__init__(
            'redis', 'qcloudcliV1', 'DescribeTaskInfo', 'redis.api.qcloud.com')

    def get_requestId(self):
        return self.get_params().get('requestId')

    def set_requestId(self, requestId):
        self.add_param('requestId', requestId)
