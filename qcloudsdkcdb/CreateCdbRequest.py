# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateCdbRequest(Request):

    def __init__(self):
        super(CreateCdbRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'CreateCdb', 'cdb.api.qcloud.com')

    def get_autoRenewFlag(self):
        return self.get_params().get('autoRenewFlag')

    def set_autoRenewFlag(self, autoRenewFlag):
        self.add_param('autoRenewFlag', autoRenewFlag)

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_cdbType(self):
        return self.get_params().get('cdbType')

    def set_cdbType(self, cdbType):
        self.add_param('cdbType', cdbType)

    def get_deployMode(self):
        return self.get_params().get('deployMode')

    def set_deployMode(self, deployMode):
        self.add_param('deployMode', deployMode)

    def get_engineVersion(self):
        return self.get_params().get('engineVersion')

    def set_engineVersion(self, engineVersion):
        self.add_param('engineVersion', engineVersion)

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_instanceRole(self):
        return self.get_params().get('instanceRole')

    def set_instanceRole(self, instanceRole):
        self.add_param('instanceRole', instanceRole)

    def get_memory(self):
        return self.get_params().get('memory')

    def set_memory(self, memory):
        self.add_param('memory', memory)

    def get_paramList(self):
        return self.get_params().get('paramList')

    def set_paramList(self, paramList):
        self.add_param('paramList', paramList)

    def get_password(self):
        return self.get_params().get('password')

    def set_password(self, password):
        self.add_param('password', password)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_port(self):
        return self.get_params().get('port')

    def set_port(self, port):
        self.add_param('port', port)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_protectMode(self):
        return self.get_params().get('protectMode')

    def set_protectMode(self, protectMode):
        self.add_param('protectMode', protectMode)

    def get_slaveZoneFirst(self):
        return self.get_params().get('slaveZoneFirst')

    def set_slaveZoneFirst(self, slaveZoneFirst):
        self.add_param('slaveZoneFirst', slaveZoneFirst)

    def get_slaveZoneSecond(self):
        return self.get_params().get('slaveZoneSecond')

    def set_slaveZoneSecond(self, slaveZoneSecond):
        self.add_param('slaveZoneSecond', slaveZoneSecond)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_volume(self):
        return self.get_params().get('volume')

    def set_volume(self, volume):
        self.add_param('volume', volume)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)

    def get_zoneId(self):
        return self.get_params().get('zoneId')

    def set_zoneId(self, zoneId):
        self.add_param('zoneId', zoneId)
