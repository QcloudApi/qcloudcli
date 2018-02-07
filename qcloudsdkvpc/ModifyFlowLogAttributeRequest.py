# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyFlowLogAttributeRequest(Request):

    def __init__(self):
        super(ModifyFlowLogAttributeRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyFlowLogAttribute', 'vpc.api.qcloud.com')

    def get_flowLogDescription(self):
        return self.get_params().get('flowLogDescription')

    def set_flowLogDescription(self, flowLogDescription):
        self.add_param('flowLogDescription', flowLogDescription)

    def get_flowLogId(self):
        return self.get_params().get('flowLogId')

    def set_flowLogId(self, flowLogId):
        self.add_param('flowLogId', flowLogId)

    def get_flowLogName(self):
        return self.get_params().get('flowLogName')

    def set_flowLogName(self, flowLogName):
        self.add_param('flowLogName', flowLogName)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
