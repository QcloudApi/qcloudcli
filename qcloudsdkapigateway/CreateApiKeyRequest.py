# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateApiKeyRequest(Request):

    def __init__(self):
        super(CreateApiKeyRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'CreateApiKey', 'apigateway.api.qcloud.com')

    def get_secretName(self):
        return self.get_params().get('secretName')

    def set_secretName(self, secretName):
        self.add_param('secretName', secretName)
