# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ManualRewriteRequest(Request):

    def __init__(self):
        super(ManualRewriteRequest, self).__init__(
            'lb', 'qcloudcliV1', 'ManualRewrite', 'lb.api.qcloud.com')

    def get_loadBalancerId(self):
        return self.get_params().get('loadBalancerId')

    def set_loadBalancerId(self, loadBalancerId):
        self.add_param('loadBalancerId', loadBalancerId)

    def get_rewriteInfo(self):
        return self.get_params().get('rewriteInfo')

    def set_rewriteInfo(self, rewriteInfo):
        self.add_param('rewriteInfo', rewriteInfo)

    def get_sourceuListenerId(self):
        return self.get_params().get('sourceuListenerId')

    def set_sourceuListenerId(self, sourceuListenerId):
        self.add_param('sourceuListenerId', sourceuListenerId)

    def get_targetuListenerId(self):
        return self.get_params().get('targetuListenerId')

    def set_targetuListenerId(self, targetuListenerId):
        self.add_param('targetuListenerId', targetuListenerId)
