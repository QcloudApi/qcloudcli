# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAlarmListRequest(Request):

    def __init__(self):
        super(DescribeAlarmListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeAlarmList', 'monitor.api.qcloud.com')

    def get_endtime(self):
        return self.get_params().get('endtime')

    def set_endtime(self, endtime):
        self.add_param('endtime', endtime)

    def get_metricName(self):
        return self.get_params().get('metricName')

    def set_metricName(self, metricName):
        self.add_param('metricName', metricName)

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)

    def get_starttime(self):
        return self.get_params().get('starttime')

    def set_starttime(self, starttime):
        self.add_param('starttime', starttime)
