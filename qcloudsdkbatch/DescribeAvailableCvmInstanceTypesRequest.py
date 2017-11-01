# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAvailableCvmInstanceTypesRequest(Request):

    def __init__(self):
        super(DescribeAvailableCvmInstanceTypesRequest, self).__init__(
            'batch', 'qcloudcliV1', 'DescribeAvailableCvmInstanceTypes', 'batch.api.qcloud.com')

    def get_Filters(self):
        return self.get_params().get('Filters')

    def set_Filters(self, Filters):
        self.add_param('Filters', Filters)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
