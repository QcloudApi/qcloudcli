# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DataSearchRequest(Request):

    def __init__(self):
        super(DataSearchRequest, self).__init__(
            'yunsou', 'qcloudcliV1', 'DataSearch', 'yunsou.api.qcloud.com')

    def get_appId(self):
        return self.get_params().get('appId')

    def set_appId(self, appId):
        self.add_param('appId', appId)

    def get_clFilter(self):
        return self.get_params().get('clFilter')

    def set_clFilter(self, clFilter):
        self.add_param('clFilter', clFilter)

    def get_distinct(self):
        return self.get_params().get('distinct')

    def set_distinct(self, distinct):
        self.add_param('distinct', distinct)

    def get_enableAbsHighlight(self):
        return self.get_params().get('enableAbsHighlight')

    def set_enableAbsHighlight(self, enableAbsHighlight):
        self.add_param('enableAbsHighlight', enableAbsHighlight)

    def get_extra(self):
        return self.get_params().get('extra')

    def set_extra(self, extra):
        self.add_param('extra', extra)

    def get_groupBy(self):
        return self.get_params().get('groupBy')

    def set_groupBy(self, groupBy):
        self.add_param('groupBy', groupBy)

    def get_isSmartbox(self):
        return self.get_params().get('isSmartbox')

    def set_isSmartbox(self, isSmartbox):
        self.add_param('isSmartbox', isSmartbox)

    def get_l4RankExpression(self):
        return self.get_params().get('l4RankExpression')

    def set_l4RankExpression(self, l4RankExpression):
        self.add_param('l4RankExpression', l4RankExpression)

    def get_latitude(self):
        return self.get_params().get('latitude')

    def set_latitude(self, latitude):
        self.add_param('latitude', latitude)

    def get_longitude(self):
        return self.get_params().get('longitude')

    def set_longitude(self, longitude):
        self.add_param('longitude', longitude)

    def get_matchValue(self):
        return self.get_params().get('matchValue')

    def set_matchValue(self, matchValue):
        self.add_param('matchValue', matchValue)

    def get_maxDocReturn(self):
        return self.get_params().get('maxDocReturn')

    def set_maxDocReturn(self, maxDocReturn):
        self.add_param('maxDocReturn', maxDocReturn)

    def get_numFilter(self):
        return self.get_params().get('numFilter')

    def set_numFilter(self, numFilter):
        self.add_param('numFilter', numFilter)

    def get_numPerPage(self):
        return self.get_params().get('numPerPage')

    def set_numPerPage(self, numPerPage):
        self.add_param('numPerPage', numPerPage)

    def get_pageId(self):
        return self.get_params().get('pageId')

    def set_pageId(self, pageId):
        self.add_param('pageId', pageId)

    def get_qcBid(self):
        return self.get_params().get('qcBid')

    def set_qcBid(self, qcBid):
        self.add_param('qcBid', qcBid)

    def get_queryEncode(self):
        return self.get_params().get('queryEncode')

    def set_queryEncode(self, queryEncode):
        self.add_param('queryEncode', queryEncode)

    def get_rankType(self):
        return self.get_params().get('rankType')

    def set_rankType(self, rankType):
        self.add_param('rankType', rankType)

    def get_searchId(self):
        return self.get_params().get('searchId')

    def set_searchId(self, searchId):
        self.add_param('searchId', searchId)

    def get_searchQuery(self):
        return self.get_params().get('searchQuery')

    def set_searchQuery(self, searchQuery):
        self.add_param('searchQuery', searchQuery)

    def get_secondSearch(self):
        return self.get_params().get('secondSearch')

    def set_secondSearch(self, secondSearch):
        self.add_param('secondSearch', secondSearch)

    def get_sourceId(self):
        return self.get_params().get('sourceId')

    def set_sourceId(self, sourceId):
        self.add_param('sourceId', sourceId)
