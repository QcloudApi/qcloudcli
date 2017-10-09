#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ListPoliciesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cam', 'qcloudcliV1', 'ListPolicies', 'cam.api.qcloud.com')

	def get_marker(self):
		return self.get_params().get('marker')

	def set_marker(self, marker):
		self.add_param('marker', marker)

	def get_isAscendingOrder(self):
		return self.get_params().get('isAscendingOrder')

	def set_isAscendingOrder(self, isAscendingOrder):
		self.add_param('isAscendingOrder', isAscendingOrder)

	def get_pageSize(self):
		return self.get_params().get('pageSize')

	def set_pageSize(self, pageSize):
		self.add_param('pageSize', pageSize)

	def get_marker(self):
		return self.get_params().get('marker')

	def set_marker(self, marker):
		self.add_param('marker', marker)

	def get_isAscendingOrder(self):
		return self.get_params().get('isAscendingOrder')

	def set_isAscendingOrder(self, isAscendingOrder):
		self.add_param('isAscendingOrder', isAscendingOrder)

	def get_pageSize(self):
		return self.get_params().get('pageSize')

	def set_pageSize(self, pageSize):
		self.add_param('pageSize', pageSize)

