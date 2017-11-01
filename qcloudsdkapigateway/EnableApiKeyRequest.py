# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EnableApiKeyRequest(Request):

    def __init__(self):
        super(EnableApiKeyRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'EnableApiKey', 'apigateway.api.qcloud.com')

    def get_secretId(self):
        return self.get_params().get('secretId')

    def set_secretId(self, secretId):
        self.add_param('secretId', secretId)
