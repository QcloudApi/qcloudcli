# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateForwardLBSeventhLayerListenersRequest(Request):

    def __init__(self):
        super(CreateForwardLBSeventhLayerListenersRequest, self).__init__(
            'lb', 'qcloudcliV1', 'CreateForwardLBSeventhLayerListeners', 'lb.api.qcloud.com')

    def get_listeners(self):
        return self.get_params().get('listeners')

    def set_listeners(self, listeners):
        self.add_param('listeners', listeners)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)
