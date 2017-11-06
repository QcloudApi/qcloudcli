# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateScalingConfigurationRequest(Request):

    def __init__(self):
        super(CreateScalingConfigurationRequest, self).__init__(
            'scaling', 'qcloudcliV1', 'CreateScalingConfiguration', 'scaling.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_bandwidthType(self):
        return self.get_params().get('bandwidthType')

    def set_bandwidthType(self, bandwidthType):
        self.add_param('bandwidthType', bandwidthType)

    def get_cpu(self):
        return self.get_params().get('cpu')

    def set_cpu(self, cpu):
        self.add_param('cpu', cpu)

    def get_cvmType(self):
        return self.get_params().get('cvmType')

    def set_cvmType(self, cvmType):
        self.add_param('cvmType', cvmType)

    def get_dataSnapshotId(self):
        return self.get_params().get('dataSnapshotId')

    def set_dataSnapshotId(self, dataSnapshotId):
        self.add_param('dataSnapshotId', dataSnapshotId)

    def get_imageId(self):
        return self.get_params().get('imageId')

    def set_imageId(self, imageId):
        self.add_param('imageId', imageId)

    def get_imageType(self):
        return self.get_params().get('imageType')

    def set_imageType(self, imageType):
        self.add_param('imageType', imageType)

    def get_keepImageSetting(self):
        return self.get_params().get('keepImageSetting')

    def set_keepImageSetting(self, keepImageSetting):
        self.add_param('keepImageSetting', keepImageSetting)

    def get_keyId(self):
        return self.get_params().get('keyId')

    def set_keyId(self, keyId):
        self.add_param('keyId', keyId)

    def get_mem(self):
        return self.get_params().get('mem')

    def set_mem(self, mem):
        self.add_param('mem', mem)

    def get_needMonitorAgent(self):
        return self.get_params().get('needMonitorAgent')

    def set_needMonitorAgent(self, needMonitorAgent):
        self.add_param('needMonitorAgent', needMonitorAgent)

    def get_needSecurityAgent(self):
        return self.get_params().get('needSecurityAgent')

    def set_needSecurityAgent(self, needSecurityAgent):
        self.add_param('needSecurityAgent', needSecurityAgent)

    def get_password(self):
        return self.get_params().get('password')

    def set_password(self, password):
        self.add_param('password', password)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_rootSize(self):
        return self.get_params().get('rootSize')

    def set_rootSize(self, rootSize):
        self.add_param('rootSize', rootSize)

    def get_scalingConfigurationName(self):
        return self.get_params().get('scalingConfigurationName')

    def set_scalingConfigurationName(self, scalingConfigurationName):
        self.add_param('scalingConfigurationName', scalingConfigurationName)

    def get_sgId(self):
        return self.get_params().get('sgId')

    def set_sgId(self, sgId):
        self.add_param('sgId', sgId)

    def get_storageSize(self):
        return self.get_params().get('storageSize')

    def set_storageSize(self, storageSize):
        self.add_param('storageSize', storageSize)

    def get_storageType(self):
        return self.get_params().get('storageType')

    def set_storageType(self, storageType):
        self.add_param('storageType', storageType)

    def get_wanIp(self):
        return self.get_params().get('wanIp')

    def set_wanIp(self, wanIp):
        self.add_param('wanIp', wanIp)
