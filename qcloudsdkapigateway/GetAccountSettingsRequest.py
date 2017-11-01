# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetAccountSettingsRequest(Request):

    def __init__(self):
        super(GetAccountSettingsRequest, self).__init__(
            'apigateway', 'qcloudcliV1', 'GetAccountSettings', 'apigateway.api.qcloud.com')
