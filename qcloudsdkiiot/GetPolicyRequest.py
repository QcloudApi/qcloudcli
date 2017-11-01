# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetPolicyRequest(Request):

    def __init__(self):
        super(GetPolicyRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'GetPolicy', 'iiot.api.qcloud.com')

    def get_policyName(self):
        return self.get_params().get('policyName')

    def set_policyName(self, policyName):
        self.add_param('policyName', policyName)
