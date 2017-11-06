# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateTiDBBetaInstancesRequest(Request):

    def __init__(self):
        super(CreateTiDBBetaInstancesRequest, self).__init__(
            'tidb', 'qcloudcliV1', 'CreateTiDBBetaInstances', 'tidb.api.qcloud.com')

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_payMode(self):
        return self.get_params().get('payMode')

    def set_payMode(self, payMode):
        self.add_param('payMode', payMode)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_region(self):
        return self.get_params().get('region')

    def set_region(self, region):
        self.add_param('region', region)

    def get_rootPassword(self):
        return self.get_params().get('rootPassword')

    def set_rootPassword(self, rootPassword):
        self.add_param('rootPassword', rootPassword)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_tidbCpu(self):
        return self.get_params().get('tidbCpu')

    def set_tidbCpu(self, tidbCpu):
        self.add_param('tidbCpu', tidbCpu)

    def get_tidbMemory(self):
        return self.get_params().get('tidbMemory')

    def set_tidbMemory(self, tidbMemory):
        self.add_param('tidbMemory', tidbMemory)

    def get_tidbNode_NodeNum(self):
        return self.get_params().get('tidbNode_NodeNum')

    def set_tidbNode_NodeNum(self, tidbNode_NodeNum):
        self.add_param('tidbNode_NodeNum', tidbNode_NodeNum)

    def get_tidbStorage(self):
        return self.get_params().get('tidbStorage')

    def set_tidbStorage(self, tidbStorage):
        self.add_param('tidbStorage', tidbStorage)

    def get_tidbVersion(self):
        return self.get_params().get('tidbVersion')

    def set_tidbVersion(self, tidbVersion):
        self.add_param('tidbVersion', tidbVersion)

    def get_tikvCpu(self):
        return self.get_params().get('tikvCpu')

    def set_tikvCpu(self, tikvCpu):
        self.add_param('tikvCpu', tikvCpu)

    def get_tikvMemory(self):
        return self.get_params().get('tikvMemory')

    def set_tikvMemory(self, tikvMemory):
        self.add_param('tikvMemory', tikvMemory)

    def get_tikvNodeNum(self):
        return self.get_params().get('tikvNodeNum')

    def set_tikvNodeNum(self, tikvNodeNum):
        self.add_param('tikvNodeNum', tikvNodeNum)

    def get_tikvStorage(self):
        return self.get_params().get('tikvStorage')

    def set_tikvStorage(self, tikvStorage):
        self.add_param('tikvStorage', tikvStorage)

    def get_tikvVersion(self):
        return self.get_params().get('tikvVersion')

    def set_tikvVersion(self, tikvVersion):
        self.add_param('tikvVersion', tikvVersion)

    def get_timeSpan(self):
        return self.get_params().get('timeSpan')

    def set_timeSpan(self, timeSpan):
        self.add_param('timeSpan', timeSpan)

    def get_timeUnit(self):
        return self.get_params().get('timeUnit')

    def set_timeUnit(self, timeUnit):
        self.add_param('timeUnit', timeUnit)

    def get_tranId(self):
        return self.get_params().get('tranId')

    def set_tranId(self, tranId):
        self.add_param('tranId', tranId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_zone(self):
        return self.get_params().get('zone')

    def set_zone(self, zone):
        self.add_param('zone', zone)

    def get_zones(self):
        return self.get_params().get('zones')

    def set_zones(self, zones):
        self.add_param('zones', zones)
