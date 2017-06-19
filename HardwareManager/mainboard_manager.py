from mainboard_dao import MainBoard
import requests
import re


class MainBoardManager:
    mainboard_url = "http://detail.zol.com.cn/motherboard/"

    ##
    # 爬帖子列表
    ##
    def __spide_mainboard(self, eachclass, page):
        __mainboard = MainBoard()
        __mainboard.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __mainboard.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __mainboard.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __mainboard.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
        if __price is not None:
            __price = __price.group(1)
        __mainboard.price = __price
        __chipset = re.search('<span>主芯片组：</span>(.*?)\t', eachclass, re.S)
        if __chipset is not None:
            __mainboard.chipset = __chipset.group(1)
        __socketType = re.search('<span>CPU插槽：</span>(.*?)\t', eachclass, re.S)
        if __socketType is not None:
            __mainboard.socketType = __socketType.group(1)
        __cpuSupport = re.search('<span>CPU类型：</span>(.*?)\t', eachclass, re.S)
        if __cpuSupport is not None:
            __mainboard.cpuSupport = __cpuSupport.group(1)
        __ddrSupport = re.search('<span>内存类型：</span>(.*?)\t', eachclass, re.S)
        if __ddrSupport is not None:
            __mainboard.ddrSupport = __ddrSupport.group(1)
        __integratedChip = re.search('<span>集成芯片：</span>(.*?)\t', eachclass, re.S)
        if __integratedChip is not None:
            __mainboard.integratedChip = __integratedChip.group(1)
        __integratedGraph = re.search('<span>显示芯片：</span>(.*?)\t', eachclass, re.S)
        if __integratedGraph is not None:
            __mainboard.integratedGraph = __integratedGraph.group(1)
        __boardSize = re.search('<span>主板板型：</span>(.*?)\t', eachclass, re.S)
        if __boardSize is not None:
            __mainboard.boardSize = __boardSize.group(1)
        __usbPort = re.search('<span>USB接口：</span>(.*?)\t', eachclass, re.S)
        if __usbPort is not None:
            __mainboard.usbPort = __usbPort.group(1)
        __zolSocre = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolSocre is not None:
            __mainboard.zolScore = __zolSocre.group(1)
        __mainboard.page = page
        return __mainboard

    def fetch_mainboards(self):
        __mainBoardDao = MainBoard()
        html = requests.get(self.mainboard_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.mainboard_url + str(page)+".html")
            __mainboard_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            mainboards = []
            for each in __mainboard_list:
                __mainboard = self.__spide_mainboard(each, page)
                mainboards.append(__mainboard)
            __mainBoardDao.save_mainboards(mainboards)

    def get_mainboards(self, page):
        __mainBoardDao = MainBoard()
        __mainboards = __mainBoardDao.get_mainboards_by_condition(None, page).all()
        return __mainboards

    def get_mainboards_count(self):
        __mainBoardDao = MainBoard()
        __count = __mainBoardDao.get_mainboards_count(None)
        return __count


if __name__ == '__main__':
    __mainboard_manager = MainBoardManager()
    __mainboard_manager.fetch_mainboards()
