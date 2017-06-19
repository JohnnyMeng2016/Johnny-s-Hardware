from graph_dao import Graph
import requests
import re



class GraphManager:
    cpu_url = "http://detail.zol.com.cn/vga/"

    ##
    # 爬帖子列表
    ##
    def __spide_graph(self, eachclass, page):
        __graph = Graph()
        __graph.zolId = re.search('data-follow-id="(.*?)">', eachclass, re.S).group(1)
        __graph.image = re.search('src="(.*?)">', eachclass, re.S).group(1)
        __graph.name = re.search('<h3>.*?target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        __category = re.search('<span class="pval">.*?target="_blank">(.*?)</a>', eachclass, re.S)
        if __category is not None:
            __category = __category.group(1)
            __category = __category.replace("\n", "")
            __category = __category.replace("\t", "")
            __graph.category = __category
        __price = re.search('<b class="price-sign">￥</b><b class="price-type">(.*?)</b>', eachclass, re.S)
        if __price is not None:
            __price = __price.group(1)
        __graph.price = __price
        __coreType = re.search('<span>芯片厂商：</span>(.*?)\t', eachclass, re.S)
        if __coreType is not None:
            __graph.coreType = __coreType.group(1)
        __chipset = re.search('<span>显卡芯片：</span>(.*?)\t', eachclass, re.S)
        if __chipset is not None:
            __graph.chipset = __chipset.group(1)
        __ram = re.search('<span>显存容量：</span>(.*?)\t', eachclass, re.S)
        if __ram is not None:
            __graph.ram = __ram.group(1)
        __bit = re.search('<span>显存位宽：</span>(.*?)\t', eachclass, re.S)
        if __bit is not None:
            __graph.bit = __bit.group(1)
        __coreFrequency = re.search('<span>核心频率：</span>(.*?)\t', eachclass, re.S)
        if __coreFrequency is not None:
            __graph.coreFrequency = __coreFrequency.group(1)
        __vmFrequency = re.search('<span>显存频率：</span>(.*?)\t', eachclass, re.S)
        if __vmFrequency is not None:
            __graph.vmFrequency = __vmFrequency.group(1)
        __fanType = re.search('<span>散热方式：</span>(.*?)\t', eachclass, re.S)
        if __fanType is not None:
            __graph.fanType = __fanType.group(1)
        __zolScore = re.search('<b>(.*?)</b>', eachclass, re.S)
        if __zolScore is not None:
            __graph.zolScore = __zolScore.group(1)
        __graph.page = page
        return __graph

    def fetch_graphs(self):
        __graph = Graph()
        html = requests.get(self.cpu_url)
        __page_count = re.search('<span class="small-page-active">.*?</b>/(.*?)</span>', html.text, re.S).group(1)
        for page in range(int(__page_count)):
            page = page + 1
            if page is not 1:
                html = requests.get(self.cpu_url + str(page)+'.html')
            __graph_list = re.findall('data-follow-id.*?<div class="price-box">.*?</div>', html.text, re.S)
            graphs = []
            for each in __graph_list:
                __graph = self.__spide_graph(each, page)
                graphs.append(__graph)
            __graph.save_graphs(graphs)

    def get_graphs(self, page):
        __graphDao = Graph()
        __graphs = __graphDao.get_graphs_by_condition(None, page).all()
        return __graphs

    def get_graph_count(self):
        __graphDao = Graph()
        __count = __graphDao.get_graph_count(None)
        return __count



if __name__ == '__main__':
    __graph_manager = GraphManager()
    __graph_manager.fetch_graphs()
    # __cpus = __cpu_manager.get_cpus(1)
    # print(__cpus)
