# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteLoadBalancersRequest(Request):

    def __init__(self):
        super(DeleteLoadBalancersRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DeleteLoadBalancers', 'lb.api.qcloud.com')

    def get_loadBalancerIds(self):
        return self.get_params().get('loadBalancerIds')

    def set_loadBalancerIds(self, loadBalancerIds):
        self.add_param('loadBalancerIds', loadBalancerIds)
