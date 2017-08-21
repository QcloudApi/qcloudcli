#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class LexicalCheckRequest(Request):

	def __init__(self):
		Request.__init__(self, 'wenzhi', 'qcloudcliV1', 'LexicalCheck', 'wenzhi.api.qcloud.com')

	def get_text(self):
		return self.get_params().get('text')

	def set_text(self, text):
		self.add_param('text', text)

