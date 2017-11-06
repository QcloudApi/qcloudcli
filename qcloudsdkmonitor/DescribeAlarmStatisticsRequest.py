# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAlarmStatisticsRequest(Request):

    def __init__(self):
        super(DescribeAlarmStatisticsRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeAlarmStatistics', 'monitor.api.qcloud.com')

    def get_metrics(self):
        return self.get_params().get('metrics')

    def set_metrics(self, metrics):
        self.add_param('metrics', metrics)

    def get_viewName(self):
        return self.get_params().get('viewName')

    def set_viewName(self, viewName):
        self.add_param('viewName', viewName)
