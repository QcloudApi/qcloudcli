# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListUsersRequest(Request):

    def __init__(self):
        super(ListUsersRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListUsers', 'cam.api.qcloud.com')
