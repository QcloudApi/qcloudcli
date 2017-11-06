# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCmemRequest(Request):

    def __init__(self):
        super(DescribeCmemRequest, self).__init__(
            'cmem', 'qcloudcliV1', 'DescribeCmem', 'cmem.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_sizeInfo(self):
        return self.get_params().get('sizeInfo')

    def set_sizeInfo(self, sizeInfo):
        self.add_param('sizeInfo', sizeInfo)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
