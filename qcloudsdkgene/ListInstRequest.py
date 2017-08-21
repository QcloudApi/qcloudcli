#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ListInstRequest(Request):

	def __init__(self):
		Request.__init__(self, 'gene', 'qcloudcliV1', 'ListInst', 'gene.api.qcloud.com')

