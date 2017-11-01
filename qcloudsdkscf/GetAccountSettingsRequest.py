# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetAccountSettingsRequest(Request):

    def __init__(self):
        super(GetAccountSettingsRequest, self).__init__(
            'scf', 'qcloudcliV1', 'GetAccountSettings', 'scf.api.qcloud.com')
