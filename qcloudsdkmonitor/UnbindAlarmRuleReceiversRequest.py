# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UnbindAlarmRuleReceiversRequest(Request):

    def __init__(self):
        super(UnbindAlarmRuleReceiversRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'UnbindAlarmRuleReceivers', 'monitor.api.qcloud.com')

    def get_alarmRuleId(self):
        return self.get_params().get('alarmRuleId')

    def set_alarmRuleId(self, alarmRuleId):
        self.add_param('alarmRuleId', alarmRuleId)
