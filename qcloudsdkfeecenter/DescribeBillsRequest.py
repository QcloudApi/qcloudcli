#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeBillsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'feecenter', 'qcloudcliV1', 'DescribeBills', 'feecenter.api.qcloud.com')

	def get_startDate(self):
		return self.get_params().get('startDate')

	def set_startDate(self, startDate):
		self.add_param('startDate', startDate)

	def get_endDate(self):
		return self.get_params().get('endDate')

	def set_endDate(self, endDate):
		self.add_param('endDate', endDate)

	def get_offset(self):
		return self.get_params().get('offset')

	def set_offset(self, offset):
		self.add_param('offset', offset)

	def get_limit(self):
		return self.get_params().get('limit')

	def set_limit(self, limit):
		self.add_param('limit', limit)

	def get_projectId(self):
		return self.get_params().get('projectId')

	def set_projectId(self, projectId):
		self.add_param('projectId', projectId)

	def get_orderType(self):
		return self.get_params().get('orderType')

	def set_orderType(self, orderType):
		self.add_param('orderType', orderType)

	def get_payerUin(self):
		return self.get_params().get('payerUin')

	def set_payerUin(self, payerUin):
		self.add_param('payerUin', payerUin)

	def get_payType(self):
		return self.get_params().get('payType')

	def set_payType(self, payType):
		self.add_param('payType', payType)

	def get_startTime(self):
		return self.get_params().get('startTime')

	def set_startTime(self, startTime):
		self.add_param('startTime', startTime)

	def get_endTime(self):
		return self.get_params().get('endTime')

	def set_endTime(self, endTime):
		self.add_param('endTime', endTime)

	def get_order(self):
		return self.get_params().get('order')

	def set_order(self, order):
		self.add_param('order', order)

