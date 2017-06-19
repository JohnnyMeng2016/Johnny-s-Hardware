from cpu_dao import Cpu
import requests
import re



class CpuManager:
    cpu_url = "http://detail.zol.com.cn/cpu/s6219/"

    ##
    # 爬帖子列表
    ##
    def __spide_cpu(self, eachclass, page):
        __cpu = Cpu()
        __cpu.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __cpu.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __cpu.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __cpu.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
        if __price is not None:
            __price = __price.group(1)
        __cpu.price = __price
        __socketType = re.search('<span>插槽类型：</span>(.*?)\t', eachclass, re.S)
        if __socketType is not None:
            __cpu.socketType = __socketType.group(1)
        __frequency = re.search('<span>CPU主频：</span>(.*?)\t', eachclass, re.S)
        if __frequency is not None:
            __cpu.frequency = __frequency.group(1)
        __turboFrequency = re.search('<span>动态加速频率：</span>(.*?)\t', eachclass, re.S)
        if __turboFrequency is not None:
            __cpu.turboFrequency = __turboFrequency.group(1)
        __craftsmanship = re.search('<span>制作工艺：</span>(.*?)\t', eachclass, re.S)
        if __craftsmanship is not None:
            __cpu.craftsmanship = __craftsmanship.group(1)
        __secondCache = re.search('<span>二级缓存：</span>(.*?)\t', eachclass, re.S)
        if __secondCache is not None:
            __cpu.secondCache = __secondCache.group(1)
        __thirdCache = re.search('<span>三级缓存：</span>(.*?)\t', eachclass, re.S)
        if __thirdCache is not None:
            __cpu.thirdCache = __thirdCache.group(1)
        __coreNum = re.search('<span>核心数量：</span>(.*?)\t', eachclass, re.S)
        if __coreNum is not None:
            __cpu.coreNum = __coreNum.group(1)
        __coreCode = re.search('<span>核心代号：</span>(.*?)\t', eachclass, re.S)
        if __coreCode is not None:
            __cpu.coreCode = __coreCode.group(1)
        __tdp = re.search('<span>热设计功耗(TDP)：</span>(.*?)\t', eachclass, re.S)
        if __tdp is not None:
            __cpu.tdp = __tdp.group(1)
        __ht = re.search('<span>总线规格：</span>(.*?)\t', eachclass, re.S)
        if __ht is not None:
            __cpu.ht = __ht.group(1)
        __zolScore = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolScore is not None:
            __cpu.zolScore = __zolScore.group(1)
        __cpu.page = page
        return __cpu

    def fetch_cpus(self):
        __cpu = Cpu()
        html = requests.get(self.cpu_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.cpu_url + str(page)+'.html')
            __cpu_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            cpus = []
            for each in __cpu_list:
                __cpu = self.__spide_cpu(each, page)
                cpus.append(__cpu)
            __cpu.save_cpus(cpus)

    def get_cpus(self, page):
        __cpuDao = Cpu()
        __cpus = __cpuDao.get_cpus_by_condition(None, page).all()
        return __cpus

    def get_cpu_count(self):
        __cpuDao = Cpu()
        __count = __cpuDao.get_cpu_count(None)
        return __count



if __name__ == '__main__':
    __cpu_manager = CpuManager()
    __cpu_manager.fetch_cpus()
    # __cpus = __cpu_manager.get_cpus(1)
    # print(__cpus)
