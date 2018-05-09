# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListGroupsRequest(Request):

    def __init__(self):
        super(ListGroupsRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListGroups', 'cam.api.qcloud.com')

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_rp(self):
        return self.get_params().get('rp')

    def set_rp(self, rp):
        self.add_param('rp', rp)
