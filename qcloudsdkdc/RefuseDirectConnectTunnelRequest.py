# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RefuseDirectConnectTunnelRequest(Request):

    def __init__(self):
        super(RefuseDirectConnectTunnelRequest, self).__init__(
            'dc', 'qcloudcliV1', 'RefuseDirectConnectTunnel', 'dc.api.qcloud.com')

    def get_directConnectTunnelId(self):
        return self.get_params().get('directConnectTunnelId')

    def set_directConnectTunnelId(self, directConnectTunnelId):
        self.add_param('directConnectTunnelId', directConnectTunnelId)
