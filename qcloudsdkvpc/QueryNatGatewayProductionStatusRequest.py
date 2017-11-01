# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class QueryNatGatewayProductionStatusRequest(Request):

    def __init__(self):
        super(QueryNatGatewayProductionStatusRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'QueryNatGatewayProductionStatus', 'vpc.api.qcloud.com')

    def get_billId(self):
        return self.get_params().get('billId')

    def set_billId(self, billId):
        self.add_param('billId', billId)
