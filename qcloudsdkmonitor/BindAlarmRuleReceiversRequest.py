#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class BindAlarmRuleReceiversRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'BindAlarmRuleReceivers', 'monitor.api.qcloud.com')

	def get_alarmRuleId(self):
		return self.get_params().get('alarmRuleId')

	def set_alarmRuleId(self, alarmRuleId):
		self.add_param('alarmRuleId', alarmRuleId)

	def get_receiversId(self):
		return self.get_params().get('receiversId')

	def set_receiversId(self, receiversId):
		self.add_param('receiversId', receiversId)

