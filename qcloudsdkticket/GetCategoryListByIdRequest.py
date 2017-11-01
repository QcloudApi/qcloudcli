# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCategoryListByIdRequest(Request):

    def __init__(self):
        super(GetCategoryListByIdRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'GetCategoryListById', 'ticket.api.qcloud.com')

    def get_level2_id(self):
        return self.get_params().get('level2_id')

    def set_level2_id(self, level2_id):
        self.add_param('level2_id', level2_id)
