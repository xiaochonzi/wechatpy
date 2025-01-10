# -*- coding: utf-8 -*-
import datetime

from wechatpy.client.api.base import BaseWeChatAPI


class WeChatPublisher(BaseWeChatAPI):
    API_BASE_URL = "https://api.weixin.qq.com/publisher/stat"

    @classmethod
    def _to_date_str(cls, date):
        if isinstance(date, datetime.date):
            return date.strftime("%Y-%m-%d")
        elif isinstance(date, str):
            return date
        else:
            raise ValueError("Can not convert %s type to str", type(date))

    def publisher_adpos_general(self, page, page_size, start_date, end_date, ad_slot=None):
        """
        获取公众号分广告位数据
        详情参考
        https://developers.weixin.qq.com/doc/offiaccount/Analytics/Ad_Analysis.html#%E4%B8%80%E3%80%81%E8%8E%B7%E5%8F%96%E5%85%AC%E4%BC%97%E5%8F%B7%E5%88%86%E5%B9%BF%E5%91%8A%E4%BD%8D%E6%95%B0%E6%8D%AE%EF%BC%88publisher-adpos-general%EF%BC%89
        """
        params = {
            "page": page,
            "page_size": page_size,
            "start_date": self._to_date_str(start_date),
            "end_date": self._to_date_str(end_date),
            "ad_slot": ad_slot
        }
        return self._get("?action=publisher_adpos_general", params=params)

    def publisher_cps_general(self, page, page_size, start_date, end_date):
        """
        获取公众号返佣商品数据
        详情参考
        https://developers.weixin.qq.com/doc/offiaccount/Analytics/Ad_Analysis.html#%E4%BA%8C%E3%80%81%E8%8E%B7%E5%8F%96%E5%85%AC%E4%BC%97%E5%8F%B7%E8%BF%94%E4%BD%A3%E5%95%86%E5%93%81%E6%95%B0%E6%8D%AE%EF%BC%88publisher-cps-general%EF%BC%89
        """
        params = {
            "page": page,
            "page_size": page_size,
            "start_date": self._to_date_str(start_date),
            "end_date": self._to_date_str(end_date),
        }
        return self._get("?action=publisher_cps_general", params=params)

    def publisher_settlement(self, page, page_size, start_date, end_date):
        """
        获取公众号结算收入数据及结算主体信息
        详情参考
        https://developers.weixin.qq.com/doc/offiaccount/Analytics/Ad_Analysis.html#%E4%B8%89%E3%80%81%E8%8E%B7%E5%8F%96%E5%85%AC%E4%BC%97%E5%8F%B7%E7%BB%93%E7%AE%97%E6%94%B6%E5%85%A5%E6%95%B0%E6%8D%AE%E5%8F%8A%E7%BB%93%E7%AE%97%E4%B8%BB%E4%BD%93%E4%BF%A1%E6%81%AF%EF%BC%88publisher-settlement%EF%BC%89
        """
        params = {
            "page": page,
            "page_size": page_size,
            "start_date": self._to_date_str(start_date),
            "end_date": self._to_date_str(end_date)
        }
        return self._get("?action=publisher_settlement", params=params)