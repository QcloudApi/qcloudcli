#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeSnapshotOpLogsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'snapshot', 'qcloudcliV1', 'DescribeSnapshotOpLogs', 'snapshot.api.qcloud.com')

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)

	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)

	def get_projectIds(self):
		return self.get_params().get('projectIds')

	def set_projectIds(self, projectIds):
		self.add_param('projectIds', projectIds)

	def get_status(self):
		return self.get_params().get('status')

	def set_status(self, status):
		self.add_param('status', status)

	def get_detail(self):
		return self.get_params().get('detail')

	def set_detail(self, detail):
		self.add_param('detail', detail)

	def get_beginTime(self):
		return self.get_params().get('beginTime')

	def set_beginTime(self, beginTime):
		self.add_param('beginTime', beginTime)

	def get_endTime(self):
		return self.get_params().get('endTime')

	def set_endTime(self, endTime):
		self.add_param('endTime', endTime)

	def get_command(self):
		return self.get_params().get('command')

	def set_command(self, command):
		self.add_param('command', command)

	def get_orderField(self):
		return self.get_params().get('orderField')

	def set_orderField(self, orderField):
		self.add_param('orderField', orderField)

	def get_order(self):
		return self.get_params().get('order')

	def set_order(self, order):
		self.add_param('order', order)

	def get_instanceId(self):
		return self.get_params().get('instanceId')

	def set_instanceId(self, instanceId):
		self.add_param('instanceId', instanceId)

