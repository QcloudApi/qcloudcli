# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeNamespaceRequest(Request):

    def __init__(self):
        super(DescribeNamespaceRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeNamespace', 'monitor.api.qcloud.com')
