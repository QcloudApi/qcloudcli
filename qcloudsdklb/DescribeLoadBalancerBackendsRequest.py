# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLoadBalancerBackendsRequest(Request):

    def __init__(self):
        super(DescribeLoadBalancerBackendsRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DescribeLoadBalancerBackends', 'lb.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
