#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetMonitorRealtimeDataRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'GetMonitorRealtimeData', 'monitor.api.qcloud.com')

	def get_namespace(self):
		return self.get_params().get('namespace')

	def set_namespace(self, namespace):
		self.add_param('namespace', namespace)

	def get_dimensions(self):
		return self.get_params().get('dimensions')

	def set_dimensions(self, dimensions):
		self.add_param('dimensions', dimensions)

	def get_period(self):
		return self.get_params().get('period')

	def set_period(self, period):
		self.add_param('period', period)

	def get_statistics(self):
		return self.get_params().get('statistics')

	def set_statistics(self, statistics):
		self.add_param('statistics', statistics)

	def get_metricName(self):
		return self.get_params().get('metricName')

	def set_metricName(self, metricName):
		self.add_param('metricName', metricName)

	def get_batch(self):
		return self.get_params().get('batch')

	def set_batch(self, batch):
		self.add_param('batch', batch)

