# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeBasicAlarmListRequest(Request):

    def __init__(self):
        super(DescribeBasicAlarmListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeBasicAlarmList', 'monitor.api.qcloud.com')

    def get_alarmStatus(self):
        return self.get_params().get('alarmStatus')

    def set_alarmStatus(self, alarmStatus):
        self.add_param('alarmStatus', alarmStatus)

    def get_dimension(self):
        return self.get_params().get('dimension')

    def set_dimension(self, dimension):
        self.add_param('dimension', dimension)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_objLike(self):
        return self.get_params().get('objLike')

    def set_objLike(self, objLike):
        self.add_param('objLike', objLike)

    def get_occurTimeOrder(self):
        return self.get_params().get('occurTimeOrder')

    def set_occurTimeOrder(self, occurTimeOrder):
        self.add_param('occurTimeOrder', occurTimeOrder)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_projectIds(self):
        return self.get_params().get('projectIds')

    def set_projectIds(self, projectIds):
        self.add_param('projectIds', projectIds)

    def get_requestType(self):
        return self.get_params().get('requestType')

    def set_requestType(self, requestType):
        self.add_param('requestType', requestType)

    def get_search(self):
        return self.get_params().get('search')

    def set_search(self, search):
        self.add_param('search', search)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_viewNames(self):
        return self.get_params().get('viewNames')

    def set_viewNames(self, viewNames):
        self.add_param('viewNames', viewNames)
