# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateCertificateRequest(Request):

    def __init__(self):
        super(UpdateCertificateRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'UpdateCertificate', 'iothub.api.qcloud.com')

    def get_certificateId(self):
        return self.get_params().get('certificateId')

    def set_certificateId(self, certificateId):
        self.add_param('certificateId', certificateId)

    def get_newStatus(self):
        return self.get_params().get('newStatus')

    def set_newStatus(self, newStatus):
        self.add_param('newStatus', newStatus)
