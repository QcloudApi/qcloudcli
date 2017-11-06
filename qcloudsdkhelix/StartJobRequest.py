# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class StartJobRequest(Request):

    def __init__(self):
        super(StartJobRequest, self).__init__(
            'helix', 'qcloudcliV1', 'StartJob', 'helix.api.qcloud.com')

    def get_cmd(self):
        return self.get_params().get('cmd')

    def set_cmd(self, cmd):
        self.add_param('cmd', cmd)

    def get_dataDiskPath(self):
        return self.get_params().get('dataDiskPath')

    def set_dataDiskPath(self, dataDiskPath):
        self.add_param('dataDiskPath', dataDiskPath)

    def get_dataDiskSize(self):
        return self.get_params().get('dataDiskSize')

    def set_dataDiskSize(self, dataDiskSize):
        self.add_param('dataDiskSize', dataDiskSize)

    def get_depend(self):
        return self.get_params().get('depend')

    def set_depend(self, depend):
        self.add_param('depend', depend)

    def get_desc(self):
        return self.get_params().get('desc')

    def set_desc(self, desc):
        self.add_param('desc', desc)

    def get_extMountPathMap(self):
        return self.get_params().get('extMountPathMap')

    def set_extMountPathMap(self, extMountPathMap):
        self.add_param('extMountPathMap', extMountPathMap)

    def get_extOutputPathMap(self):
        return self.get_params().get('extOutputPathMap')

    def set_extOutputPathMap(self, extOutputPathMap):
        self.add_param('extOutputPathMap', extOutputPathMap)

    def get_imgId(self):
        return self.get_params().get('imgId')

    def set_imgId(self, imgId):
        self.add_param('imgId', imgId)

    def get_instanceType(self):
        return self.get_params().get('instanceType')

    def set_instanceType(self, instanceType):
        self.add_param('instanceType', instanceType)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)

    def get_priority(self):
        return self.get_params().get('priority')

    def set_priority(self, priority):
        self.add_param('priority', priority)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_projectLocalPath(self):
        return self.get_params().get('projectLocalPath')

    def set_projectLocalPath(self, projectLocalPath):
        self.add_param('projectLocalPath', projectLocalPath)

    def get_rootPassword(self):
        return self.get_params().get('rootPassword')

    def set_rootPassword(self, rootPassword):
        self.add_param('rootPassword', rootPassword)

    def get_secretId(self):
        return self.get_params().get('secretId')

    def set_secretId(self, secretId):
        self.add_param('secretId', secretId)

    def get_secretKey(self):
        return self.get_params().get('secretKey')

    def set_secretKey(self, secretKey):
        self.add_param('secretKey', secretKey)

    def get_subnetid(self):
        return self.get_params().get('subnetid')

    def set_subnetid(self, subnetid):
        self.add_param('subnetid', subnetid)

    def get_sysDiskType(self):
        return self.get_params().get('sysDiskType')

    def set_sysDiskType(self, sysDiskType):
        self.add_param('sysDiskType', sysDiskType)

    def get_taskDesc(self):
        return self.get_params().get('taskDesc')

    def set_taskDesc(self, taskDesc):
        self.add_param('taskDesc', taskDesc)

    def get_taskName(self):
        return self.get_params().get('taskName')

    def set_taskName(self, taskName):
        self.add_param('taskName', taskName)

    def get_tasks(self):
        return self.get_params().get('tasks')

    def set_tasks(self, tasks):
        self.add_param('tasks', tasks)

    def get_timeout(self):
        return self.get_params().get('timeout')

    def set_timeout(self, timeout):
        self.add_param('timeout', timeout)

    def get_vpcid(self):
        return self.get_params().get('vpcid')

    def set_vpcid(self, vpcid):
        self.add_param('vpcid', vpcid)

    def get_zone(self):
        return self.get_params().get('zone')

    def set_zone(self, zone):
        self.add_param('zone', zone)
