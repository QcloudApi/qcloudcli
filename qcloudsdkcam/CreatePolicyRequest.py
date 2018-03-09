# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreatePolicyRequest(Request):

    def __init__(self):
        super(CreatePolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'CreatePolicy', 'cam.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_policyDocument(self):
        return self.get_params().get('policyDocument')

    def set_policyDocument(self, policyDocument):
        self.add_param('policyDocument', policyDocument)

    def get_policyName(self):
        return self.get_params().get('policyName')

    def set_policyName(self, policyName):
        self.add_param('policyName', policyName)
