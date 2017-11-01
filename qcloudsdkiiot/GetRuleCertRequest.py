# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetRuleCertRequest(Request):

    def __init__(self):
        super(GetRuleCertRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'GetRuleCert', 'iiot.api.qcloud.com')

    def get_commonName(self):
        return self.get_params().get('commonName')

    def set_commonName(self, commonName):
        self.add_param('commonName', commonName)
