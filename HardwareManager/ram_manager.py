from ram_dao import Ram
import requests
import re


class RamManager:
    ram_url = "http://detail.zol.com.cn/memory/s5974/"

    ##
    # 爬帖子列表
    ##
    def __spide_ram(self, eachclass, page):
        __ram = Ram()
        __ram.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __ram.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __ram.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __ram.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
        if __price is not None:
            __price = __price.group(1)
        __ram.price = __price
        __size = re.search('<span>内存容量：</span>(.*?)\t', eachclass, re.S)
        if __size is not None:
            __ram.size = __size.group(1)
        __desc = re.search('<span>容量描述：</span>(.*?)\t', eachclass, re.S)
        if __desc is not None:
            __ram.desc = __desc.group(1)
        __ddrType = re.search('<span>内存类型：</span>(.*?)\t', eachclass, re.S)
        if __ddrType is not None:
            __ram.ddrType = __ddrType.group(1)
        __frequency = re.search('<span>内存主频：</span>(.*?)\t', eachclass, re.S)
        if __frequency is not None:
            __ram.frequency = __frequency.group(1)
        __cl = re.search('<span>CL延迟：</span>(.*?)\t', eachclass, re.S)
        if __cl is not None:
            __ram.cl = __cl.group(1)
        __voltage = re.search('<span>工作电压：</span>(.*?)\t', eachclass, re.S)
        if __voltage is not None:
            __ram.voltage = __voltage.group(1)
        __pin = re.search('<span>针脚数：</span>(.*?)\t', eachclass, re.S)
        if __pin is not None:
            __ram.pin = __pin.group(1)
        __zolScore = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolScore is not None:
            __ram.zolScore = __zolScore.group(1)
        __ram.page = page
        return __ram

    def fetch_rams(self):
        __ram = Ram()
        html = requests.get(self.ram_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.ram_url + str(page) + '.html')
            __ram_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            rams = []
            for each in __ram_list:
                __ram = self.__spide_ram(each, page)
                rams.append(__ram)
            __ram.save_rams(rams)

    def get_rams(self, page):
        __ramDao = Ram()
        __cpus = __ramDao.get_rams_by_condition(None, page).all()
        return __cpus

    def get_ram_count(self):
        __ramDao = Ram()
        __count = __ramDao.get_ram_count(None)
        return __count


if __name__ == '__main__':
    __ram_manager = RamManager()
    __ram_manager.fetch_rams()
    # __cpus = __cpu_manager.get_cpus(1)
    # print(__cpus)
