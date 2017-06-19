from case_dao import Case
import requests
import re



class CaseManager:
    case_url = "http://detail.zol.com.cn/case/"

    ##
    # 爬帖子列表
    ##
    def __spide_case(self, eachclass, page):
        __case = Case()
        __case.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __case.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __case.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __case.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
        if __price is not None:
            __price = __price.group(1)
        __case.price = __price
        __caseType = re.search('<span>机箱类型：</span>(.*?)\t', eachclass, re.S)
        if __caseType is not None:
            __case.caseType = __caseType.group(1)
        __structure = re.search('<span>机箱结构：</span>(.*?)\t', eachclass, re.S)
        if __structure is not None:
            __case.structure = __structure.group(1)
        __smallPosition = re.search('<span>3.5英寸仓位：</span>(.*?)\t', eachclass, re.S)
        if __smallPosition is not None:
            __case.smallPosition = __smallPosition.group(1)
        __bigPosition = re.search('<span>5.25英寸仓位：</span>(.*?)\t', eachclass, re.S)
        if __bigPosition is not None:
            __case.bigPosition = __bigPosition.group(1)
        __panelPort = re.search('<span>面板接口：</span>(.*?)\t', eachclass, re.S)
        if __panelPort is not None:
            __case.panelPort = __panelPort.group(1)
        __caseMaterial = re.search('<span>机箱材质：</span>(.*?)\t', eachclass, re.S)
        if __caseMaterial is not None:
            __case.caseMaterial = __caseMaterial.group(1)
        __extSlot = re.search('<span>扩展插槽：</span>(.*?)\t', eachclass, re.S)
        if __extSlot is not None:
            __case.extSlot = __extSlot.group(1)
        __caseTheme = re.search('<span>机箱样式：</span>(.*?)\t', eachclass, re.S)
        if __caseTheme is not None:
            __case.caseTheme = __caseTheme.group(1)
        __powerSupport = re.search('<span>电源类型：</span>(.*?)\t', eachclass, re.S)
        if __powerSupport is not None:
            __case.powerSupport = __powerSupport.group(1)
        __weight = re.search('<span>产品重量：</span>(.*?)\t', eachclass, re.S)
        if __weight is not None:
            __case.weight = __weight.group(1)
        __lineMode = re.search('<span>理线功能：</span>(.*?)\t', eachclass, re.S)
        if __lineMode is not None:
            __case.lineMode = __lineMode.group(1)
        __mainboardSupport = re.search('<span>适用主板：</span>(.*?)\t', eachclass, re.S)
        if __mainboardSupport is not None:
            __case.mainboardSupport = __mainboardSupport.group(1)
        __fan = re.search('<span>散热性能：</span>(.*?)\t', eachclass, re.S)
        if __fan is not None:
            __case.fan = __fan.group(1)
        __zolScore = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolScore is not None:
            __case.zolScore = __zolScore.group(1)
        __case.page = page
        return __case

    def fetch_cases(self):
        __case = Case()
        html = requests.get(self.case_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.case_url + str(page)+'.html')
            __case_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            cases = []
            for each in __case_list:
                __case = self.__spide_case(each, page)
                cases.append(__case)
            __case.save_cases(cases)

    def get_cases(self, page):
        __caseDao = Case()
        __cases = __caseDao.get_cases_by_condition(None, page).all()
        return __cases

    def get_case_count(self):
        __caseDao = Case()
        __count = __caseDao.get_case_count(None)
        return __count



if __name__ == '__main__':
    __case_manager = CaseManager()
    __case_manager.fetch_cases()
    # __cpus = __cpu_manager.get_cpus(1)
    # print(__cpus)
