# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetUserBaseInfoRequest(Request):

    def __init__(self):
        super(GetUserBaseInfoRequest, self).__init__(
            'open', 'qcloudcliV1', 'GetUserBaseInfo', 'open.api.qcloud.com')
