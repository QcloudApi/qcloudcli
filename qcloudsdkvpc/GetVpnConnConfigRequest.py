# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetVpnConnConfigRequest(Request):

    def __init__(self):
        super(GetVpnConnConfigRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'GetVpnConnConfig', 'vpc.api.qcloud.com')

    def get_interfaceName(self):
        return self.get_params().get('interfaceName')

    def set_interfaceName(self, interfaceName):
        self.add_param('interfaceName', interfaceName)

    def get_platform(self):
        return self.get_params().get('platform')

    def set_platform(self, platform):
        self.add_param('platform', platform)

    def get_software(self):
        return self.get_params().get('software')

    def set_software(self, software):
        self.add_param('software', software)

    def get_vendorname(self):
        return self.get_params().get('vendorname')

    def set_vendorname(self, vendorname):
        self.add_param('vendorname', vendorname)

    def get_vpnConnId(self):
        return self.get_params().get('vpnConnId')

    def set_vpnConnId(self, vpnConnId):
        self.add_param('vpnConnId', vpnConnId)
