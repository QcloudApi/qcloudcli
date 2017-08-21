#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class QuotaGetRequest(Request):

	def __init__(self):
		Request.__init__(self, 'wenzhi', 'qcloudcliV1', 'QuotaGet', 'wenzhi.api.qcloud.com')

