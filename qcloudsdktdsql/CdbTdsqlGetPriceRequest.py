# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetPriceRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetPriceRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetPrice', 'tdsql.api.qcloud.com')

    def get_costType(self):
        return self.get_params().get('costType')

    def set_costType(self, costType):
        self.add_param('costType', costType)

    def get_dbType(self):
        return self.get_params().get('dbType')

    def set_dbType(self, dbType):
        self.add_param('dbType', dbType)

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)
