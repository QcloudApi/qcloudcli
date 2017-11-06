# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateServiceRequest(Request):

    def __init__(self):
        super(CreateServiceRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'CreateService', 'apigateway.api.qcloud.com')

    def get_protocol(self):
        return self.get_params().get('protocol')

    def set_protocol(self, protocol):
        self.add_param('protocol', protocol)

    def get_serviceDesc(self):
        return self.get_params().get('serviceDesc')

    def set_serviceDesc(self, serviceDesc):
        self.add_param('serviceDesc', serviceDesc)

    def get_serviceName(self):
        return self.get_params().get('serviceName')

    def set_serviceName(self, serviceName):
        self.add_param('serviceName', serviceName)
