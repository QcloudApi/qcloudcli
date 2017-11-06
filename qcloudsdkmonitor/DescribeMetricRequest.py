# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeMetricRequest(Request):

    def __init__(self):
        super(DescribeMetricRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeMetric', 'monitor.api.qcloud.com')

    def get_metricName(self):
        return self.get_params().get('metricName')

    def set_metricName(self, metricName):
        self.add_param('metricName', metricName)

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)
