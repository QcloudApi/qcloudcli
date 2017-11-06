# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class InquiryCdbPriceHourRequest(Request):

    def __init__(self):
        super(InquiryCdbPriceHourRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'InquiryCdbPriceHour', 'cdb.api.qcloud.com')

    def get_cdbType(self):
        return self.get_params().get('cdbType')

    def set_cdbType(self, cdbType):
        self.add_param('cdbType', cdbType)

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_instanceRole(self):
        return self.get_params().get('instanceRole')

    def set_instanceRole(self, instanceRole):
        self.add_param('instanceRole', instanceRole)

    def get_memory(self):
        return self.get_params().get('memory')

    def set_memory(self, memory):
        self.add_param('memory', memory)

    def get_protectMode(self):
        return self.get_params().get('protectMode')

    def set_protectMode(self, protectMode):
        self.add_param('protectMode', protectMode)

    def get_volume(self):
        return self.get_params().get('volume')

    def set_volume(self, volume):
        self.add_param('volume', volume)

    def get_zoneId(self):
        return self.get_params().get('zoneId')

    def set_zoneId(self, zoneId):
        self.add_param('zoneId', zoneId)
