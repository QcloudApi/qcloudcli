# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateEipRequest(Request):

    def __init__(self):
        super(CreateEipRequest, self).__init__(
            'eip', 'qcloudcliV1', 'CreateEip', 'eip.api.qcloud.com')

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_ispId(self):
        return self.get_params().get('ispId')

    def set_ispId(self, ispId):
        self.add_param('ispId', ispId)

    def get_tgwGroup(self):
        return self.get_params().get('tgwGroup')

    def set_tgwGroup(self, tgwGroup):
        self.add_param('tgwGroup', tgwGroup)
