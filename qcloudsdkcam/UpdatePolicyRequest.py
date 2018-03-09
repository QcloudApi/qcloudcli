# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdatePolicyRequest(Request):

    def __init__(self):
        super(UpdatePolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'UpdatePolicy', 'cam.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_policyDocument(self):
        return self.get_params().get('policyDocument')

    def set_policyDocument(self, policyDocument):
        self.add_param('policyDocument', policyDocument)

    def get_policyId(self):
        return self.get_params().get('policyId')

    def set_policyId(self, policyId):
        self.add_param('policyId', policyId)

    def get_policyName(self):
        return self.get_params().get('policyName')

    def set_policyName(self, policyName):
        self.add_param('policyName', policyName)
