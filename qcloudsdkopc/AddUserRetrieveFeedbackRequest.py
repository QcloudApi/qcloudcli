#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class AddUserRetrieveFeedbackRequest(Request):

	def __init__(self):
		Request.__init__(self, 'opc', 'qcloudcliV1', 'AddUserRetrieveFeedback', 'opc.api.qcloud.com')

	def get_data(self):
		return self.get_params().get('data')

	def set_data(self, data):
		self.add_param('data', data)

