# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateAlarmRuleRequest(Request):

    def __init__(self):
        super(CreateAlarmRuleRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'CreateAlarmRule', 'monitor.api.qcloud.com')

    def get_constancy(self):
        return self.get_params().get('constancy')

    def set_constancy(self, constancy):
        self.add_param('constancy', constancy)

    def get_metricName(self):
        return self.get_params().get('metricName')

    def set_metricName(self, metricName):
        self.add_param('metricName', metricName)

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)

    def get_operatorType(self):
        return self.get_params().get('operatorType')

    def set_operatorType(self, operatorType):
        self.add_param('operatorType', operatorType)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_statistics(self):
        return self.get_params().get('statistics')

    def set_statistics(self, statistics):
        self.add_param('statistics', statistics)

    def get_threshold(self):
        return self.get_params().get('threshold')

    def set_threshold(self, threshold):
        self.add_param('threshold', threshold)
