# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeBmLoadBalancersTaskResultRequest(Request):

    def __init__(self):
        super(DescribeBmLoadBalancersTaskResultRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DescribeBmLoadBalancersTaskResult', 'lb.api.qcloud.com')

    def get_requestId(self):
        return self.get_params().get('requestId')

    def set_requestId(self, requestId):
        self.add_param('requestId', requestId)
