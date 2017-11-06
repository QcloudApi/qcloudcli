# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeObjectsRequest(Request):

    def __init__(self):
        super(DescribeObjectsRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeObjects', 'monitor.api.qcloud.com')

    def get_dimensionNames(self):
        return self.get_params().get('dimensionNames')

    def set_dimensionNames(self, dimensionNames):
        self.add_param('dimensionNames', dimensionNames)

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
