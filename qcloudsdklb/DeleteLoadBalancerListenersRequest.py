# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteLoadBalancerListenersRequest(Request):

    def __init__(self):
        super(DeleteLoadBalancerListenersRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DeleteLoadBalancerListeners', 'lb.api.qcloud.com')

    def get_listenerIds(self):
        return self.get_params().get('listenerIds')

    def set_listenerIds(self, listenerIds):
        self.add_param('listenerIds', listenerIds)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)
