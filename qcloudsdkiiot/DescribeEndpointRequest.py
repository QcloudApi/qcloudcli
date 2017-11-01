# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeEndpointRequest(Request):

    def __init__(self):
        super(DescribeEndpointRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'DescribeEndpoint', 'iiot.api.qcloud.com')
