# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyAlarmRuleRequest(Request):

    def __init__(self):
        super(ModifyAlarmRuleRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'ModifyAlarmRule', 'monitor.api.qcloud.com')

    def get_alarmRuleId(self):
        return self.get_params().get('alarmRuleId')

    def set_alarmRuleId(self, alarmRuleId):
        self.add_param('alarmRuleId', alarmRuleId)

    def get_constancy(self):
        return self.get_params().get('constancy')

    def set_constancy(self, constancy):
        self.add_param('constancy', constancy)

    def get_operatorType(self):
        return self.get_params().get('operatorType')

    def set_operatorType(self, operatorType):
        self.add_param('operatorType', operatorType)

    def get_receiversId(self):
        return self.get_params().get('receiversId')

    def set_receiversId(self, receiversId):
        self.add_param('receiversId', receiversId)

    def get_threshold(self):
        return self.get_params().get('threshold')

    def set_threshold(self, threshold):
        self.add_param('threshold', threshold)
