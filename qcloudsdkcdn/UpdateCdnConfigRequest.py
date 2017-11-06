# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateCdnConfigRequest(Request):

    def __init__(self):
        super(UpdateCdnConfigRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'UpdateCdnConfig', 'cdn.api.qcloud.com')

    def get_accessIp(self):
        return self.get_params().get('accessIp')

    def set_accessIp(self, accessIp):
        self.add_param('accessIp', accessIp)

    def get_advancedCache(self):
        return self.get_params().get('advancedCache')

    def set_advancedCache(self, advancedCache):
        self.add_param('advancedCache', advancedCache)

    def get_advancedMaxage(self):
        return self.get_params().get('advancedMaxage')

    def set_advancedMaxage(self, advancedMaxage):
        self.add_param('advancedMaxage', advancedMaxage)

    def get_backupOrigin(self):
        return self.get_params().get('backupOrigin')

    def set_backupOrigin(self, backupOrigin):
        self.add_param('backupOrigin', backupOrigin)

    def get_cache(self):
        return self.get_params().get('cache')

    def set_cache(self, cache):
        self.add_param('cache', cache)

    def get_cacheMode(self):
        return self.get_params().get('cacheMode')

    def set_cacheMode(self, cacheMode):
        self.add_param('cacheMode', cacheMode)

    def get_capping(self):
        return self.get_params().get('capping')

    def set_capping(self, capping):
        self.add_param('capping', capping)

    def get_compression(self):
        return self.get_params().get('compression')

    def set_compression(self, compression):
        self.add_param('compression', compression)

    def get_dedicateLine(self):
        return self.get_params().get('dedicateLine')

    def set_dedicateLine(self, dedicateLine):
        self.add_param('dedicateLine', dedicateLine)

    def get_detailReqHeader(self):
        return self.get_params().get('detailReqHeader')

    def set_detailReqHeader(self, detailReqHeader):
        self.add_param('detailReqHeader', detailReqHeader)

    def get_detailRspHeader(self):
        return self.get_params().get('detailRspHeader')

    def set_detailRspHeader(self, detailRspHeader):
        self.add_param('detailRspHeader', detailRspHeader)

    def get_fullUrl(self):
        return self.get_params().get('fullUrl')

    def set_fullUrl(self, fullUrl):
        self.add_param('fullUrl', fullUrl)

    def get_furlCache(self):
        return self.get_params().get('furlCache')

    def set_furlCache(self, furlCache):
        self.add_param('furlCache', furlCache)

    def get_fwdHost(self):
        return self.get_params().get('fwdHost')

    def set_fwdHost(self, fwdHost):
        self.add_param('fwdHost', fwdHost)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)

    def get_ignoreCacheControl(self):
        return self.get_params().get('ignoreCacheControl')

    def set_ignoreCacheControl(self, ignoreCacheControl):
        self.add_param('ignoreCacheControl', ignoreCacheControl)

    def get_ignoreSetCookie(self):
        return self.get_params().get('ignoreSetCookie')

    def set_ignoreSetCookie(self, ignoreSetCookie):
        self.add_param('ignoreSetCookie', ignoreSetCookie)

    def get_middleResource(self):
        return self.get_params().get('middleResource')

    def set_middleResource(self, middleResource):
        self.add_param('middleResource', middleResource)

    def get_origin(self):
        return self.get_params().get('origin')

    def set_origin(self, origin):
        self.add_param('origin', origin)

    def get_pathRefer(self):
        return self.get_params().get('pathRefer')

    def set_pathRefer(self, pathRefer):
        self.add_param('pathRefer', pathRefer)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_refer(self):
        return self.get_params().get('refer')

    def set_refer(self, refer):
        self.add_param('refer', refer)

    def get_reqHeader(self):
        return self.get_params().get('reqHeader')

    def set_reqHeader(self, reqHeader):
        self.add_param('reqHeader', reqHeader)

    def get_rspHeader(self):
        return self.get_params().get('rspHeader')

    def set_rspHeader(self, rspHeader):
        self.add_param('rspHeader', rspHeader)

    def get_statusCache(self):
        return self.get_params().get('statusCache')

    def set_statusCache(self, statusCache):
        self.add_param('statusCache', statusCache)

    def get_videoSwitch(self):
        return self.get_params().get('videoSwitch')

    def set_videoSwitch(self, videoSwitch):
        self.add_param('videoSwitch', videoSwitch)
