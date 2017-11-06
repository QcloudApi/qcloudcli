# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlCreateInstanceRequest(Request):

    def __init__(self):
        super(CdbTdsqlCreateInstanceRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlCreateInstance', 'tdsql.api.qcloud.com')

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

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
