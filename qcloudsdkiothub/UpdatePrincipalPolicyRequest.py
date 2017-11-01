# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdatePrincipalPolicyRequest(Request):

    def __init__(self):
        super(UpdatePrincipalPolicyRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'UpdatePrincipalPolicy', 'iothub.api.qcloud.com')

    def get_policyName(self):
        return self.get_params().get('policyName')

    def set_policyName(self, policyName):
        self.add_param('policyName', policyName)

    def get_principal(self):
        return self.get_params().get('principal')

    def set_principal(self, principal):
        self.add_param('principal', principal)
