# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateApiRequest(Request):

    def __init__(self):
        super(CreateApiRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'CreateApi', 'apigateway.api.qcloud.com')

    def get_apiDesc(self):
        return self.get_params().get('apiDesc')

    def set_apiDesc(self, apiDesc):
        self.add_param('apiDesc', apiDesc)

    def get_authRequired(self):
        return self.get_params().get('authRequired')

    def set_authRequired(self, authRequired):
        self.add_param('authRequired', authRequired)

    def get_requestConfig(self):
        return self.get_params().get('requestConfig')

    def set_requestConfig(self, requestConfig):
        self.add_param('requestConfig', requestConfig)

    def get_requestParameters(self):
        return self.get_params().get('requestParameters')

    def set_requestParameters(self, requestParameters):
        self.add_param('requestParameters', requestParameters)

    def get_serviceConfig(self):
        return self.get_params().get('serviceConfig')

    def set_serviceConfig(self, serviceConfig):
        self.add_param('serviceConfig', serviceConfig)

    def get_serviceId(self):
        return self.get_params().get('serviceId')

    def set_serviceId(self, serviceId):
        self.add_param('serviceId', serviceId)

    def get_serviceMockReturnMessage(self):
        return self.get_params().get('serviceMockReturnMessage')

    def set_serviceMockReturnMessage(self, serviceMockReturnMessage):
        self.add_param('serviceMockReturnMessage', serviceMockReturnMessage)

    def get_serviceParameters(self):
        return self.get_params().get('serviceParameters')

    def set_serviceParameters(self, serviceParameters):
        self.add_param('serviceParameters', serviceParameters)

    def get_serviceScfFunctionName(self):
        return self.get_params().get('serviceScfFunctionName')

    def set_serviceScfFunctionName(self, serviceScfFunctionName):
        self.add_param('serviceScfFunctionName', serviceScfFunctionName)

    def get_serviceTimeout(self):
        return self.get_params().get('serviceTimeout')

    def set_serviceTimeout(self, serviceTimeout):
        self.add_param('serviceTimeout', serviceTimeout)

    def get_serviceType(self):
        return self.get_params().get('serviceType')

    def set_serviceType(self, serviceType):
        self.add_param('serviceType', serviceType)
