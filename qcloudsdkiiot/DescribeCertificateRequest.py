# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCertificateRequest(Request):

    def __init__(self):
        super(DescribeCertificateRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'DescribeCertificate', 'iiot.api.qcloud.com')

    def get_certificateId(self):
        return self.get_params().get('certificateId')

    def set_certificateId(self, certificateId):
        self.add_param('certificateId', certificateId)
