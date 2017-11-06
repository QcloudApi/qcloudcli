# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLoadBalancerListenersRequest(Request):

    def __init__(self):
        super(DescribeLoadBalancerListenersRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DescribeLoadBalancerListeners', 'lb.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_listenerIds(self):
        return self.get_params().get('listenerIds')

    def set_listenerIds(self, listenerIds):
        self.add_param('listenerIds', listenerIds)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_loadBalancerPort(self):
        return self.get_params().get('loadBalancerPort')

    def set_loadBalancerPort(self, loadBalancerPort):
        self.add_param('loadBalancerPort', loadBalancerPort)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_protocol(self):
        return self.get_params().get('protocol')

    def set_protocol(self, protocol):
        self.add_param('protocol', protocol)

    def get_status(self):
        return self.get_params().get('status')

    def set_status(self, status):
        self.add_param('status', status)
