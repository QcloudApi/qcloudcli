#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class CreateProjectRequest(Request):

	def __init__(self):
		Request.__init__(self, 'gene', 'qcloudcliV1', 'CreateProject', 'gene.api.qcloud.com')

