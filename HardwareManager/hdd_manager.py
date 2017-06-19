from hdd_dao import Hdd
import requests
import re



class HddManager:
    hdd_url = "http://detail.zol.com.cn/hard_drives/"

    ##
    # 爬帖子列表
    ##
    def __spide_hdd(self, eachclass, page):
        __hdd = Hdd()
        __hdd.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __hdd.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __hdd.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __hdd.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
        if __price is not None:
            __price = __price.group(1)
        __hdd.price = __price
        __size = re.search('<span>硬盘容量：</span>(.*?)\t', eachclass, re.S)
        if __size is not None:
            __hdd.size = __size.group(1)
        __port = re.search('<span>接口类型：</span>(.*?)\t', eachclass, re.S)
        if __port is not None:
            __hdd.port = __port.group(1)
        __type = re.search('<span>适用类型：</span>(.*?)\t', eachclass, re.S)
        if __type is not None:
            __hdd.type = __type.group(1)
        __rpm = re.search('<span>转速：</span>(.*?)\t', eachclass, re.S)
        if __rpm is not None:
            __hdd.rpm = __rpm.group(1)
        __cache = re.search('<span>缓存：</span>(.*?)\t', eachclass, re.S)
        if __cache is not None:
            __hdd.cache = __cache.group(1)
        __portBit = re.search('<span>接口速率：</span>(.*?)\t', eachclass, re.S)
        if __portBit is not None:
            __hdd.portBit = __portBit.group(1)
        __inchType = re.search('<span>硬盘尺寸：</span>(.*?)\t', eachclass, re.S)
        if __inchType is not None:
            __hdd.inchType = __inchType.group(1)
        __zolScore = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolScore is not None:
            __hdd.zolScore = __zolScore.group(1)
        __hdd.page = page
        return __hdd

    def fetch_hdds(self):
        __hdd = Hdd()
        html = requests.get(self.hdd_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.hdd_url + str(page)+'.html')
            __hdd_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            hdds = []
            for each in __hdd_list:
                __hdd = self.__spide_hdd(each, page)
                hdds.append(__hdd)
            __hdd.save_hdds(hdds)

    def get_hdds(self, page):
        __hddDao = Hdd()
        __hdds = __hddDao.get_hdds_by_condition(None, page).all()
        return __hdds

    def get_hdd_count(self):
        __hddDao = Hdd()
        __count = __hddDao.get_hdd_count(None)
        return __count



if __name__ == '__main__':
    __hdd_manager = HddManager()
    __hdd_manager.fetch_hdds()
    # __cpus = __cpu_manager.get_cpus(1)
    # print(__cpus)
