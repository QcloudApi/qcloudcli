# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteDirectConnectTunnelRequest(Request):

    def __init__(self):
        super(DeleteDirectConnectTunnelRequest, self).__init__(
            'dc', 'qcloudcliV1', 'DeleteDirectConnectTunnel', 'dc.api.qcloud.com')

    def get_directConnectTunnelId(self):
        return self.get_params().get('directConnectTunnelId')

    def set_directConnectTunnelId(self, directConnectTunnelId):
        self.add_param('directConnectTunnelId', directConnectTunnelId)
