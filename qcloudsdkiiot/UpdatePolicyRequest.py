# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdatePolicyRequest(Request):

    def __init__(self):
        super(UpdatePolicyRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'UpdatePolicy', 'iiot.api.qcloud.com')

    def get_policyDocument(self):
        return self.get_params().get('policyDocument')

    def set_policyDocument(self, policyDocument):
        self.add_param('policyDocument', policyDocument)

    def get_policyName(self):
        return self.get_params().get('policyName')

    def set_policyName(self, policyName):
        self.add_param('policyName', policyName)

    def get_policyRemark(self):
        return self.get_params().get('policyRemark')

    def set_policyRemark(self, policyRemark):
        self.add_param('policyRemark', policyRemark)
