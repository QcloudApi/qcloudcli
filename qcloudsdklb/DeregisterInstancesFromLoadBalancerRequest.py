# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeregisterInstancesFromLoadBalancerRequest(Request):

    def __init__(self):
        super(DeregisterInstancesFromLoadBalancerRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DeregisterInstancesFromLoadBalancer', 'lb.api.qcloud.com')

    def get_backends(self):
        return self.get_params().get('backends')

    def set_backends(self, backends):
        self.add_param('backends', backends)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)
