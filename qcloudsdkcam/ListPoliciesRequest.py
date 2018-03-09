# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListPoliciesRequest(Request):

    def __init__(self):
        super(ListPoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListPolicies', 'cam.api.qcloud.com')

    def get_keyword(self):
        return self.get_params().get('keyword')

    def set_keyword(self, keyword):
        self.add_param('keyword', keyword)

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_rp(self):
        return self.get_params().get('rp')

    def set_rp(self, rp):
        self.add_param('rp', rp)

    def get_scope(self):
        return self.get_params().get('scope')

    def set_scope(self, scope):
        self.add_param('scope', scope)
