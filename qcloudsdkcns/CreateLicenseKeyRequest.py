# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateLicenseKeyRequest(Request):

    def __init__(self):
        super(CreateLicenseKeyRequest, self).__init__(
            'cns', 'qcloudcliV1', 'CreateLicenseKey', 'cns.api.qcloud.com')

    def get_ip(self):
        return self.get_params().get('ip')

    def set_ip(self, ip):
        self.add_param('ip', ip)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
