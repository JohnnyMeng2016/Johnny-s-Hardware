from ssd_dao import SSD
import requests
import re



class SsdManager:
    ssd_url = "http://detail.zol.com.cn/solid_state_drive/"

    ##
    # 爬帖子列表
    ##
    def __spide_ssd(self, eachclass, page):
        __ssd = SSD()
        __ssd.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __ssd.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __ssd.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __ssd.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)-', eachclass, re.S)
        if __price is not None:
            __ssd.price = __price.group(1)
        else:
            __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
            if __price is not None:
                __ssd.price = __price.group(1)
        __size = re.search('<span>存储容量：</span>(.*?)\t', eachclass, re.S)
        if __size is not None:
            __ssd.size = __size.group(1)
        __port = re.search('<span>接口类型：</span>(.*?)\t', eachclass, re.S)
        if __port is not None:
            __ssd.port = __port.group(1)
        __readSpeed = re.search('<span>读取速度：</span>(.*?)\t', eachclass, re.S)
        if __readSpeed is not None:
            __ssd.readSpeed = __readSpeed.group(1)
        __writeSpeed = re.search('<span>写入速度：</span>(.*?)\t', eachclass, re.S)
        if __writeSpeed is not None:
            __ssd.writeSpeed = __writeSpeed.group(1)
        __inchType = re.search('<span>硬盘尺寸：</span>(.*?)\t', eachclass, re.S)
        if __inchType is not None:
            __ssd.inchType = __inchType.group(1)
        __warranty = re.search('<span>质保期限：</span>(.*?)\t', eachclass, re.S)
        if __warranty is not None:
            __ssd.warranty = __warranty.group(1)
        __architecture = re.search('<span>闪存架构：</span>(.*?)\t', eachclass, re.S)
        if __architecture is not None:
            __ssd.architecture = __architecture.group(1)
        __chipset = re.search('<span>主控芯片：</span>(.*?)\t', eachclass, re.S)
        if __chipset is not None:
            __ssd.chipset = __chipset.group(1)
        __seekTime = re.search('<span>平均寻道时间：</span>(.*?)\t', eachclass, re.S)
        if __seekTime is not None:
            __ssd.seekTime = __seekTime.group(1)
        __fourKRandom = re.search('<span>4K随机读：</span>(.*?)\t', eachclass, re.S)
        if __fourKRandom is not None:
            __ssd.fourKRandom = __fourKRandom.group(1)
        __zolScore = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolScore is not None:
            __ssd.zolScore = __zolScore.group(1)
        __ssd.page = page
        return __ssd

    def fetch_ssds(self):
        __ssd = SSD()
        html = requests.get(self.ssd_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.ssd_url + str(page)+'.html')
            __ssd_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            ssds = []
            for each in __ssd_list:
                __ssd = self.__spide_ssd(each, page)
                ssds.append(__ssd)
            __ssd.save_ssds(ssds)

    def get_ssds(self, page):
        __ssdDao = SSD()
        __ssds = __ssdDao.get_ssds_by_condition(None, page).all()
        return __ssds

    def get_ssd_count(self):
        __ssdDao = SSD()
        __count = __ssdDao.get_ssd_count(None)
        return __count



if __name__ == '__main__':
    __ssd_manager = SsdManager()
    __ssd_manager.fetch_ssds()
    # __cpus = __cpu_manager.get_cpus(1)
    # print(__cpus)
