# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetSubLoginUinListRequest(Request):

    def __init__(self):
        super(GetSubLoginUinListRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetSubLoginUinList', 'cam.api.qcloud.com')
