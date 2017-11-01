# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListEntitiesForPolicyRequest(Request):

    def __init__(self):
        super(ListEntitiesForPolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListEntitiesForPolicy', 'cam.api.qcloud.com')

    def get_policyId(self):
        return self.get_params().get('policyId')

    def set_policyId(self, policyId):
        self.add_param('policyId', policyId)
