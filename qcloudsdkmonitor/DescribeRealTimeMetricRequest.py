# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRealTimeMetricRequest(Request):

    def __init__(self):
        super(DescribeRealTimeMetricRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeRealTimeMetric', 'monitor.api.qcloud.com')

    def get_alarmMetricName(self):
        return self.get_params().get('alarmMetricName')

    def set_alarmMetricName(self, alarmMetricName):
        self.add_param('alarmMetricName', alarmMetricName)

    def get_dimensions(self):
        return self.get_params().get('dimensions')

    def set_dimensions(self, dimensions):
        self.add_param('dimensions', dimensions)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_metricName(self):
        return self.get_params().get('metricName')

    def set_metricName(self, metricName):
        self.add_param('metricName', metricName)

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_sort(self):
        return self.get_params().get('sort')

    def set_sort(self, sort):
        self.add_param('sort', sort)
