#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CancelJobRequest(Request):

	def __init__(self):
		Request.__init__(self, 'gene', 'qcloudcliV1', 'CancelJob', 'gene.api.qcloud.com')

