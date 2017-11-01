# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetContactListRequest(Request):

    def __init__(self):
        super(GetContactListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'GetContactList', 'monitor.api.qcloud.com')

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)
