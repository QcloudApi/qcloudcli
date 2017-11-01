# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeEndpointRequest(Request):

    def __init__(self):
        super(DescribeEndpointRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'DescribeEndpoint', 'iothub.api.qcloud.com')
