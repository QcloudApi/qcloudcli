# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetMapDataListRequest(Request):

    def __init__(self):
        super(GetMapDataListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'GetMapDataList', 'monitor.api.qcloud.com')
