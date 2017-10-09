#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeAlarmStatisticsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'DescribeAlarmStatistics', 'monitor.api.qcloud.com')

	def get_viewName(self):
		return self.get_params().get('viewName')

	def set_viewName(self, viewName):
		self.add_param('viewName', viewName)

	def get_metrics(self):
		return self.get_params().get('metrics')

	def set_metrics(self, metrics):
		self.add_param('metrics', metrics)

