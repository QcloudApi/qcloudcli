# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListGroupsForUserRequest(Request):

    def __init__(self):
        super(ListGroupsForUserRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListGroupsForUser', 'cam.api.qcloud.com')

    def get_page(self):
        return self.get_params().get('page')

    def set_page(self, page):
        self.add_param('page', page)

    def get_rp(self):
        return self.get_params().get('rp')

    def set_rp(self, rp):
        self.add_param('rp', rp)
