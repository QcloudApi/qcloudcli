# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateFlowLogRequest(Request):

    def __init__(self):
        super(CreateFlowLogRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'CreateFlowLog', 'vpc.api.qcloud.com')

    def get_cloudLogId(self):
        return self.get_params().get('cloudLogId')

    def set_cloudLogId(self, cloudLogId):
        self.add_param('cloudLogId', cloudLogId)

    def get_flowLogDescription(self):
        return self.get_params().get('flowLogDescription')

    def set_flowLogDescription(self, flowLogDescription):
        self.add_param('flowLogDescription', flowLogDescription)

    def get_flowLogName(self):
        return self.get_params().get('flowLogName')

    def set_flowLogName(self, flowLogName):
        self.add_param('flowLogName', flowLogName)

    def get_resourceId(self):
        return self.get_params().get('resourceId')

    def set_resourceId(self, resourceId):
        self.add_param('resourceId', resourceId)

    def get_resourceType(self):
        return self.get_params().get('resourceType')

    def set_resourceType(self, resourceType):
        self.add_param('resourceType', resourceType)

    def get_trafficType(self):
        return self.get_params().get('trafficType')

    def set_trafficType(self, trafficType):
        self.add_param('trafficType', trafficType)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
