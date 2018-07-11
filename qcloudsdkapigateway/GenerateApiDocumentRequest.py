# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GenerateApiDocumentRequest(Request):

    def __init__(self):
        super(GenerateApiDocumentRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'GenerateApiDocument', 'apigateway.api.qcloud.com')

    def get_environment(self):
        return self.get_params().get('environment')

    def set_environment(self, environment):
        self.add_param('environment', environment)

    def get_language(self):
        return self.get_params().get('language')

    def set_language(self, language):
        self.add_param('language', language)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)
