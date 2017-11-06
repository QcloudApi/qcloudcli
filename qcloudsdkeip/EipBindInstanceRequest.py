# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EipBindInstanceRequest(Request):

    def __init__(self):
        super(EipBindInstanceRequest, self).__init__(
            'eip', 'qcloudcliV1', 'EipBindInstance', 'eip.api.qcloud.com')

    def get_eipId(self):
        return self.get_params().get('eipId')

    def set_eipId(self, eipId):
        self.add_param('eipId', eipId)

    def get_mode(self):
        return self.get_params().get('mode')

    def set_mode(self, mode):
        self.add_param('mode', mode)

    def get_networkInterfaceId(self):
        return self.get_params().get('networkInterfaceId')

    def set_networkInterfaceId(self, networkInterfaceId):
        self.add_param('networkInterfaceId', networkInterfaceId)

    def get_privateIpAddress(self):
        return self.get_params().get('privateIpAddress')

    def set_privateIpAddress(self, privateIpAddress):
        self.add_param('privateIpAddress', privateIpAddress)

    def get_unInstanceId(self):
        return self.get_params().get('unInstanceId')

    def set_unInstanceId(self, unInstanceId):
        self.add_param('unInstanceId', unInstanceId)
