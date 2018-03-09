# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListAttachedUserPoliciesRequest(Request):

    def __init__(self):
        super(ListAttachedUserPoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListAttachedUserPolicies', 'cam.api.qcloud.com')

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_rp(self):
        return self.get_params().get('rp')

    def set_rp(self, rp):
        self.add_param('rp', rp)

    def get_uin(self):
        return self.get_params().get('uin')

    def set_uin(self, uin):
        self.add_param('uin', uin)
