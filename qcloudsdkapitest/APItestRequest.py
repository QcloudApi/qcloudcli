#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class APItestRequest(Request):

	def __init__(self):
		Request.__init__(self, 'apitest', 'qcloudcliV1', 'APItest', 'apitest.api.qcloud.com')

