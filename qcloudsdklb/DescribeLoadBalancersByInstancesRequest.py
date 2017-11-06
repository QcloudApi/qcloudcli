# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLoadBalancersByInstancesRequest(Request):

    def __init__(self):
        super(DescribeLoadBalancersByInstancesRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DescribeLoadBalancersByInstances', 'lb.api.qcloud.com')

    def get_backendInstanceName(self):
        return self.get_params().get('backendInstanceName')

    def set_backendInstanceName(self, backendInstanceName):
        self.add_param('backendInstanceName', backendInstanceName)

    def get_backendIps(self):
        return self.get_params().get('backendIps')

    def set_backendIps(self, backendIps):
        self.add_param('backendIps', backendIps)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
