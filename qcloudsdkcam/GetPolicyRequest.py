# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetPolicyRequest(Request):

    def __init__(self):
        super(GetPolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetPolicy', 'cam.api.qcloud.com')

    def get_policyId(self):
        return self.get_params().get('policyId')

    def set_policyId(self, policyId):
        self.add_param('policyId', policyId)
