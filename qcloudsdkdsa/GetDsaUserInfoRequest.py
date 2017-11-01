# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDsaUserInfoRequest(Request):

    def __init__(self):
        super(GetDsaUserInfoRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'GetDsaUserInfo', 'dsa.api.qcloud.com')
