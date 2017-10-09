#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeProductRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iothub', 'qcloudcliV1', 'DescribeProduct', 'iothub.api.qcloud.com')

	def get_productName(self):
		return self.get_params().get('productName')

	def set_productName(self, productName):
		self.add_param('productName', productName)

	def get_productName(self):
		return self.get_params().get('productName')

	def set_productName(self, productName):
		self.add_param('productName', productName)

