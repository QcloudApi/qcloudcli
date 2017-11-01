# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteBmLoadBalancersRequest(Request):

    def __init__(self):
        super(DeleteBmLoadBalancersRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DeleteBmLoadBalancers', 'lb.api.qcloud.com')

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)
