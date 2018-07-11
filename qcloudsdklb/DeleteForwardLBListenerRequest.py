# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteForwardLBListenerRequest(Request):

    def __init__(self):
        super(DeleteForwardLBListenerRequest, self).__init__(
            'lb', 'qcloudcliV1', 'DeleteForwardLBListener', 'lb.api.qcloud.com')

    def get_listenerId(self):
        return self.get_params().get('listenerId')

    def set_listenerId(self, listenerId):
        self.add_param('listenerId', listenerId)

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_loadBalancerPort(self):
        return self.get_params().get('loadBalancerPort')

    def set_loadBalancerPort(self, loadBalancerPort):
        self.add_param('loadBalancerPort', loadBalancerPort)

    def get_protocol(self):
        return self.get_params().get('protocol')

    def set_protocol(self, protocol):
        self.add_param('protocol', protocol)
