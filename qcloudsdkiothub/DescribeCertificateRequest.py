# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCertificateRequest(Request):

    def __init__(self):
        super(DescribeCertificateRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'DescribeCertificate', 'iothub.api.qcloud.com')

    def get_certificateId(self):
        return self.get_params().get('certificateId')

    def set_certificateId(self, certificateId):
        self.add_param('certificateId', certificateId)
