# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EipUnBindInstanceRequest(Request):

    def __init__(self):
        super(EipUnBindInstanceRequest, self).__init__(
            'eip', 'qcloudcliV1', 'EipUnBindInstance', 'eip.api.qcloud.com')

    def get_allocWanIp(self):
        return self.get_params().get('allocWanIp')

    def set_allocWanIp(self, allocWanIp):
        self.add_param('allocWanIp', allocWanIp)

    def get_eipId(self):
        return self.get_params().get('eipId')

    def set_eipId(self, eipId):
        self.add_param('eipId', eipId)

    def get_networkInterfaceId(self):
        return self.get_params().get('networkInterfaceId')

    def set_networkInterfaceId(self, networkInterfaceId):
        self.add_param('networkInterfaceId', networkInterfaceId)

    def get_privateIpAddress(self):
        return self.get_params().get('privateIpAddress')

    def set_privateIpAddress(self, privateIpAddress):
        self.add_param('privateIpAddress', privateIpAddress)

    def get_unBindPrivateIpWithEip(self):
        return self.get_params().get('unBindPrivateIpWithEip')

    def set_unBindPrivateIpWithEip(self, unBindPrivateIpWithEip):
        self.add_param('unBindPrivateIpWithEip', unBindPrivateIpWithEip)
