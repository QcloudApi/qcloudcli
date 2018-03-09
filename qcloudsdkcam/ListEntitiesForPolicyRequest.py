# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListEntitiesForPolicyRequest(Request):

    def __init__(self):
        super(ListEntitiesForPolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListEntitiesForPolicy', 'cam.api.qcloud.com')

    def get_entityFilter(self):
        return self.get_params().get('entityFilter')

    def set_entityFilter(self, entityFilter):
        self.add_param('entityFilter', entityFilter)

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_policyId(self):
        return self.get_params().get('policyId')

    def set_policyId(self, policyId):
        self.add_param('policyId', policyId)

    def get_rp(self):
        return self.get_params().get('rp')

    def set_rp(self, rp):
        self.add_param('rp', rp)
