# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCategoryFieldListByIdRequest(Request):

    def __init__(self):
        super(GetCategoryFieldListByIdRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'GetCategoryFieldListById', 'ticket.api.qcloud.com')

    def get_level3_id(self):
        return self.get_params().get('level3_id')

    def set_level3_id(self, level3_id):
        self.add_param('level3_id', level3_id)
