# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeDBInstancesV3Request(Request):

    def __init__(self):
        super(DescribeDBInstancesV3Request, self).__init__(
            'cdb', 'qcloudcliV1', 'DescribeDBInstancesV3', 'cdb.api.qcloud.com')

    def get_cdbErrors(self):
        return self.get_params().get('cdbErrors')

    def set_cdbErrors(self, cdbErrors):
        self.add_param('cdbErrors', cdbErrors)

    def get_engineVersions(self):
        return self.get_params().get('engineVersions')

    def set_engineVersions(self, engineVersions):
        self.add_param('engineVersions', engineVersions)

    def get_exClusterId(self):
        return self.get_params().get('exClusterId')

    def set_exClusterId(self, exClusterId):
        self.add_param('exClusterId', exClusterId)

    def get_initFlag(self):
        return self.get_params().get('initFlag')

    def set_initFlag(self, initFlag):
        self.add_param('initFlag', initFlag)

    def get_instanceIds(self):
        return self.get_params().get('instanceIds')

    def set_instanceIds(self, instanceIds):
        self.add_param('instanceIds', instanceIds)

    def get_instanceNames(self):
        return self.get_params().get('instanceNames')

    def set_instanceNames(self, instanceNames):
        self.add_param('instanceNames', instanceNames)

    def get_instanceTypes(self):
        return self.get_params().get('instanceTypes')

    def set_instanceTypes(self, instanceTypes):
        self.add_param('instanceTypes', instanceTypes)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_orderDirection(self):
        return self.get_params().get('orderDirection')

    def set_orderDirection(self, orderDirection):
        self.add_param('orderDirection', orderDirection)

    def get_payTypes(self):
        return self.get_params().get('payTypes')

    def set_payTypes(self, payTypes):
        self.add_param('payTypes', payTypes)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_regionId(self):
        return self.get_params().get('regionId')

    def set_regionId(self, regionId):
        self.add_param('regionId', regionId)

    def get_securityGroupId(self):
        return self.get_params().get('securityGroupId')

    def set_securityGroupId(self, securityGroupId):
        self.add_param('securityGroupId', securityGroupId)

    def get_status(self):
        return self.get_params().get('status')

    def set_status(self, status):
        self.add_param('status', status)

    def get_subnetIds(self):
        return self.get_params().get('subnetIds')

    def set_subnetIds(self, subnetIds):
        self.add_param('subnetIds', subnetIds)

    def get_taskStatus(self):
        return self.get_params().get('taskStatus')

    def set_taskStatus(self, taskStatus):
        self.add_param('taskStatus', taskStatus)

    def get_vips(self):
        return self.get_params().get('vips')

    def set_vips(self, vips):
        self.add_param('vips', vips)

    def get_vpcIds(self):
        return self.get_params().get('vpcIds')

    def set_vpcIds(self, vpcIds):
        self.add_param('vpcIds', vpcIds)

    def get_withExCluster(self):
        return self.get_params().get('withExCluster')

    def set_withExCluster(self, withExCluster):
        self.add_param('withExCluster', withExCluster)

    def get_withSecurityGroup(self):
        return self.get_params().get('withSecurityGroup')

    def set_withSecurityGroup(self, withSecurityGroup):
        self.add_param('withSecurityGroup', withSecurityGroup)

    def get_zoneIds(self):
        return self.get_params().get('zoneIds')

    def set_zoneIds(self, zoneIds):
        self.add_param('zoneIds', zoneIds)
