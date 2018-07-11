# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyForwardLBNameRequest(Request):

    def __init__(self):
        super(ModifyForwardLBNameRequest, self).__init__(
            'lb', 'qcloudcliV1', 'ModifyForwardLBName', 'lb.api.qcloud.com')

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_loadBalancerName(self):
        return self.get_params().get('loadBalancerName')

    def set_loadBalancerName(self, loadBalancerName):
        self.add_param('loadBalancerName', loadBalancerName)
