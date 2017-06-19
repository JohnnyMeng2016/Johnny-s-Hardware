from power_dao import Power
import requests
import re


class PowerManager:
    power_url = "http://detail.zol.com.cn/power/"

    ##
    # 爬帖子列表
    ##
    def __spide_power(self, eachclass, page):
        __power = Power()
        __power.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __power.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __power.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __power.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
        if __price is not None:
            __price = __price.group(1)
        __power.price = __price
        __ratedPower = re.search('<span>额定功率：</span>(.*?)\t', eachclass, re.S)
        if __ratedPower is not None:
            __power.ratedPower = __ratedPower.group(1)
        __maxPower = re.search('<span>最大功率：</span>(.*?)\t', eachclass, re.S)
        if __maxPower is not None:
            __power.maxPower = __maxPower.group(1)
        __powerVersion = re.search('<span>电源版本：</span>(.*?)\t', eachclass, re.S)
        if __powerVersion is not None:
            __power.powerVersion = __powerVersion.group(1)
        __support = re.search('<span>适用范围：</span>(.*?)\t', eachclass, re.S)
        if __support is not None:
            __power.support = __support.group(1)
        __fan = re.search('<span>风扇描述：</span>(.*?)\t', eachclass, re.S)
        if __fan is not None:
            __power.fan = __fan.group(1)
        __powerType = re.search('<span>电源类型：</span>(.*?)\t', eachclass, re.S)
        if __powerType is not None:
            __power.powerType = __powerType.group(1)
        __other = re.search('<span>其他特点：</span>(.*?)\t', eachclass, re.S)
        if __other is not None:
            __power.other = __other.group(1)
        __plusAuth = re.search('<span>80PLUS认证：</span>(.*?)\t', eachclass, re.S)
        if __plusAuth is not None:
            __power.plusAuth = __plusAuth.group(1)
        __safeAuth = re.search('<span>安规认证：</span>(.*?)\t', eachclass, re.S)
        if __safeAuth is not None:
            __power.safeAuth = __safeAuth.group(1)
        __pfc = re.search('<span>PFC类型：</span>(.*?)\t', eachclass, re.S)
        if __pfc is not None:
            __power.pfc = __pfc.group(1)
        __safeFunction = re.search('<span>保护功能：</span>(.*?)\t', eachclass, re.S)
        if __safeFunction is not None:
            __power.__safeFunction = __safeFunction.group(1)
        __voltageSupport = re.search('<span>交流输入：</span>(.*?)\t', eachclass, re.S)
        if __voltageSupport is not None:
            __power.voltageSupport = __voltageSupport.group(1)
        __lineMode = re.search('<span>出线类型：</span>(.*?)\t', eachclass, re.S)
        if __lineMode is not None:
            __power.lineMode = __lineMode.group(1)
        __zolScore = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolScore is not None:
            __power.zolScore = __zolScore.group(1)
        __power.page = page
        return __power

    def fetch_powers(self):
        __power = Power()
        html = requests.get(self.power_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.power_url + str(page) + '.html')
            __power_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            powers = []
            for each in __power_list:
                __power = self.__spide_power(each, page)
                powers.append(__power)
            __power.save_powers(powers)

    def get_powers(self, page):
        __powerDao = Power()
        __powers = __powerDao.get_powers_by_condition(None, page)
        return __powers

    def get_powers_by_condition(self, condition, page):
        __powerDao = Power()
        __powers = __powerDao.get_powers_by_condition(condition, page)
        return __powers;

    def get_power_count(self):
        __powerDao = Power()
        __count = __powerDao.get_power_count(None)
        return __count

    def get_power_count_by_condition(self, condition):
        __powerDao = Power()
        __count = __powerDao.get_power_count(condition)
        return __count

    def sync_powers(self):
        __powerDao = Power()
        __powerDao.delete_all_powers()
        self.fetch_powers()


if __name__ == '__main__':
    __power_manager = PowerManager()
    __power_manager.fetch_powers()
    # __cpus = __cpu_manager.get_cpus(1)
    # print(__cpus)
