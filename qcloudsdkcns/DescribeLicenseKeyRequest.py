# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLicenseKeyRequest(Request):

    def __init__(self):
        super(DescribeLicenseKeyRequest, self).__init__(
            'cns', 'qcloudcliV1', 'DescribeLicenseKey', 'cns.api.qcloud.com')

    def get_end(self):
        return self.get_params().get('end')

    def set_end(self, end):
        self.add_param('end', end)

    def get_start(self):
        return self.get_params().get('start')

    def set_start(self, start):
        self.add_param('start', start)

    def get_used(self):
        return self.get_params().get('used')

    def set_used(self, used):
        self.add_param('used', used)
