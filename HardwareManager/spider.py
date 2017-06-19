from cpu_dao import Cpu
from cpu_manager import CpuManager
import requests
import re

cpu_url = "http://detail.zol.com.cn/cpu/s6219/"

##
# 爬帖子列表
##
def __spide_cpu(eachclass):
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
    __price = re.search('<span class="">￥(.*?)</span>', eachclass, re.S)
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
    __cpu.zolScore = re.search('<b>(.*?)</b>', eachclass, re.S).group(1)
    return __cpu


if __name__=='__main__':
    html = requests.get(cpu_url)
    cpu_list = re.findall('data-follow-id.*?查询底价', html.text, re.S)
    cpus = []
    for each in cpu_list:
        __cpu = __spide_cpu(each)
        cpus.append(__cpu)
    cpu_manager = CpuManager()
    cpu_manager.save_cpus(cpus)
