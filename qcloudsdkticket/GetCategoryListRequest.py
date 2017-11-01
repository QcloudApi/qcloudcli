# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCategoryListRequest(Request):

    def __init__(self):
        super(GetCategoryListRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'GetCategoryList', 'ticket.api.qcloud.com')
