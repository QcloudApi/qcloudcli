# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RunApiRequest(Request):

    def __init__(self):
        super(RunApiRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'RunApi', 'apigateway.api.qcloud.com')

    def get_apiId(self):
        return self.get_params().get('apiId')

    def set_apiId(self, apiId):
        self.add_param('apiId', apiId)

    def get_requestBody(self):
        return self.get_params().get('requestBody')

    def set_requestBody(self, requestBody):
        self.add_param('requestBody', requestBody)

    def get_requestHeader(self):
        return self.get_params().get('requestHeader')

    def set_requestHeader(self, requestHeader):
        self.add_param('requestHeader', requestHeader)

    def get_requestMethod(self):
        return self.get_params().get('requestMethod')

    def set_requestMethod(self, requestMethod):
        self.add_param('requestMethod', requestMethod)

    def get_requestPath(self):
        return self.get_params().get('requestPath')

    def set_requestPath(self, requestPath):
        self.add_param('requestPath', requestPath)

    def get_requestQuery(self):
        return self.get_params().get('requestQuery')

    def set_requestQuery(self, requestQuery):
        self.add_param('requestQuery', requestQuery)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)
