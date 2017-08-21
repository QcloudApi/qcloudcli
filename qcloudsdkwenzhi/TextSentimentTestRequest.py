#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class TextSentimentTestRequest(Request):

	def __init__(self):
		Request.__init__(self, 'wenzhi', 'qcloudcliV1', 'TextSentimentTest', 'wenzhi.api.qcloud.com')

	def get_content(self):
		return self.get_params().get('content')

	def set_content(self, content):
		self.add_param('content', content)

	def get_type(self):
		return self.get_params().get('type')

	def set_type(self, type):
		self.add_param('type', type)

