# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetProductEventListRequest(Request):

    def __init__(self):
        super(GetProductEventListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'GetProductEventList', 'monitor.api.qcloud.com')

    def get_dimensions(self):
        return self.get_params().get('dimensions')

    def set_dimensions(self, dimensions):
        self.add_param('dimensions', dimensions)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_eventName(self):
        return self.get_params().get('eventName')

    def set_eventName(self, eventName):
        self.add_param('eventName', eventName)

    def get_instanceId(self):
        return self.get_params().get('instanceId')

    def set_instanceId(self, instanceId):
        self.add_param('instanceId', instanceId)

    def get_isAlarmConfig(self):
        return self.get_params().get('isAlarmConfig')

    def set_isAlarmConfig(self, isAlarmConfig):
        self.add_param('isAlarmConfig', isAlarmConfig)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_timeOrder(self):
        return self.get_params().get('timeOrder')

    def set_timeOrder(self, timeOrder):
        self.add_param('timeOrder', timeOrder)
