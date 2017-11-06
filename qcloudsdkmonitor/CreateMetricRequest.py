# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateMetricRequest(Request):

    def __init__(self):
        super(CreateMetricRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'CreateMetric', 'monitor.api.qcloud.com')

    def get_metricCname(self):
        return self.get_params().get('metricCname')

    def set_metricCname(self, metricCname):
        self.add_param('metricCname', metricCname)

    def get_metricName(self):
        return self.get_params().get('metricName')

    def set_metricName(self, metricName):
        self.add_param('metricName', metricName)

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)

    def get_unit(self):
        return self.get_params().get('unit')

    def set_unit(self, unit):
        self.add_param('unit', unit)
