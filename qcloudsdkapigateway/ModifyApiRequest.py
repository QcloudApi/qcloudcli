# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyApiRequest(Request):

    def __init__(self):
        super(ModifyApiRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'ModifyApi', 'apigateway.api.qcloud.com')

    def get_apiDesc(self):
        return self.get_params().get('apiDesc')

    def set_apiDesc(self, apiDesc):
        self.add_param('apiDesc', apiDesc)

    def get_apiId(self):
        return self.get_params().get('apiId')

    def set_apiId(self, apiId):
        self.add_param('apiId', apiId)

    def get_apiName(self):
        return self.get_params().get('apiName')

    def set_apiName(self, apiName):
        self.add_param('apiName', apiName)

    def get_authRequired(self):
        return self.get_params().get('authRequired')

    def set_authRequired(self, authRequired):
        self.add_param('authRequired', authRequired)

    def get_constantParameters(self):
        return self.get_params().get('constantParameters')

    def set_constantParameters(self, constantParameters):
        self.add_param('constantParameters', constantParameters)

    def get_enableCORS(self):
        return self.get_params().get('enableCORS')

    def set_enableCORS(self, enableCORS):
        self.add_param('enableCORS', enableCORS)

    def get_isDeleteResponseErrorCodes(self):
        return self.get_params().get('isDeleteResponseErrorCodes')

    def set_isDeleteResponseErrorCodes(self, isDeleteResponseErrorCodes):
        self.add_param('isDeleteResponseErrorCodes', isDeleteResponseErrorCodes)

    def get_protocol(self):
        return self.get_params().get('protocol')

    def set_protocol(self, protocol):
        self.add_param('protocol', protocol)

    def get_requestConfig(self):
        return self.get_params().get('requestConfig')

    def set_requestConfig(self, requestConfig):
        self.add_param('requestConfig', requestConfig)

    def get_requestParameters(self):
        return self.get_params().get('requestParameters')

    def set_requestParameters(self, requestParameters):
        self.add_param('requestParameters', requestParameters)

    def get_responseErrorCodes(self):
        return self.get_params().get('responseErrorCodes')

    def set_responseErrorCodes(self, responseErrorCodes):
        self.add_param('responseErrorCodes', responseErrorCodes)

    def get_responseFailExample(self):
        return self.get_params().get('responseFailExample')

    def set_responseFailExample(self, responseFailExample):
        self.add_param('responseFailExample', responseFailExample)

    def get_responseSuccessExample(self):
        return self.get_params().get('responseSuccessExample')

    def set_responseSuccessExample(self, responseSuccessExample):
        self.add_param('responseSuccessExample', responseSuccessExample)

    def get_responseType(self):
        return self.get_params().get('responseType')

    def set_responseType(self, responseType):
        self.add_param('responseType', responseType)

    def get_resultConfig(self):
        return self.get_params().get('resultConfig')

    def set_resultConfig(self, resultConfig):
        self.add_param('resultConfig', resultConfig)

    def get_resultParameters(self):
        return self.get_params().get('resultParameters')

    def set_resultParameters(self, resultParameters):
        self.add_param('resultParameters', resultParameters)

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

    def get_serviceTsfHealthCheckConf(self):
        return self.get_params().get('serviceTsfHealthCheckConf')

    def set_serviceTsfHealthCheckConf(self, serviceTsfHealthCheckConf):
        self.add_param('serviceTsfHealthCheckConf', serviceTsfHealthCheckConf)

    def get_serviceTsfLoadBalanceConf(self):
        return self.get_params().get('serviceTsfLoadBalanceConf')

    def set_serviceTsfLoadBalanceConf(self, serviceTsfLoadBalanceConf):
        self.add_param('serviceTsfLoadBalanceConf', serviceTsfLoadBalanceConf)

    def get_serviceType(self):
        return self.get_params().get('serviceType')

    def set_serviceType(self, serviceType):
        self.add_param('serviceType', serviceType)

    def get_serviceWebsocketCleanupFunctionName(self):
        return self.get_params().get('serviceWebsocketCleanupFunctionName')

    def set_serviceWebsocketCleanupFunctionName(self, serviceWebsocketCleanupFunctionName):
        self.add_param('serviceWebsocketCleanupFunctionName', serviceWebsocketCleanupFunctionName)

    def get_serviceWebsocketRegisterFunctionName(self):
        return self.get_params().get('serviceWebsocketRegisterFunctionName')

    def set_serviceWebsocketRegisterFunctionName(self, serviceWebsocketRegisterFunctionName):
        self.add_param('serviceWebsocketRegisterFunctionName', serviceWebsocketRegisterFunctionName)

    def get_serviceWebsocketTransportFunctionName(self):
        return self.get_params().get('serviceWebsocketTransportFunctionName')

    def set_serviceWebsocketTransportFunctionName(self, serviceWebsocketTransportFunctionName):
        self.add_param('serviceWebsocketTransportFunctionName', serviceWebsocketTransportFunctionName)
