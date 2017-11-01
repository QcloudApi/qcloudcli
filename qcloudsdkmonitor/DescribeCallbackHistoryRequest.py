# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCallbackHistoryRequest(Request):

    def __init__(self):
        super(DescribeCallbackHistoryRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeCallbackHistory', 'monitor.api.qcloud.com')
