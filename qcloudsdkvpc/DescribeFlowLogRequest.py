# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeFlowLogRequest(Request):

    def __init__(self):
        super(DescribeFlowLogRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeFlowLog', 'vpc.api.qcloud.com')

    def get_flowLogId(self):
        return self.get_params().get('flowLogId')

    def set_flowLogId(self, flowLogId):
        self.add_param('flowLogId', flowLogId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
