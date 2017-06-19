from flask import Flask, redirect, url_for, jsonify
from flask import request, render_template, abort
from user_manager import usermanger
from cpu_manager import CpuManager
from mainboard_manager import MainBoardManager
from ram_manager import RamManager
from hdd_manager import HddManager
from ssd_manager import SsdManager
from graph_manager import GraphManager
from case_manager import CaseManager
from power_manager import PowerManager
from view_helper import PageInfo
import config

app = Flask(__name__, )


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Public/login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    __username = request.form['username']
    __password = request.form['password']
    __usermanger = usermanger()
    if __usermanger.login(__username, __password):
        return jsonify(result=True)
    else:
        return jsonify(result=False)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/Node/index', methods=['GET', 'POST'])
def node():
    return render_template('Node/index.html')


@app.route('/User/index', methods=['GET', 'POST'])
def user():
    __usermanger = usermanger()
    __users = __usermanger.get_user_list()
    return render_template('User/index.html', users=__users)


@app.route('/User/add', methods=['GET', 'POST'])
def user_add():
    return render_template('User/add.html')


@app.route('/User/edit/<userId>', methods=['GET', 'POST'])
def user_edit(userId):
    __usermanger = usermanger()
    __user = __usermanger.get_user_by_condition(userId, None)
    return render_template('User/edit.html', user=__user)


@app.route('/Cpu/index/<page>', methods=['GET', 'POST'])
def cpu(page):
    __cpuManager = CpuManager()
    __cpus = __cpuManager.get_cpus(page)
    __count = __cpuManager.get_cpu_count()
    __pageInfo = PageInfo()
    __pageInfo.currentPage = page
    __pageInfo.recordCount = __count
    __pageCount = int(__count / config.pageSize) + 1
    __pageInfo.pageCount = __pageCount
    __pageInfo.nextPage = int(page) + 1
    __pageInfo.prePage = int(page) - 1
    return render_template('Cpu/index.html', cpus=__cpus, pageInfo=__pageInfo)


@app.route('/Mainboard/index/<page>', methods=['GET', 'POST'])
def mainboard(page):
    __mainBoardManager = MainBoardManager()
    __mainboards = __mainBoardManager.get_mainboards(page)
    __count = __mainBoardManager.get_mainboards_count()
    __pageInfo = PageInfo()
    __pageInfo.currentPage = page
    __pageInfo.recordCount = __count
    __pageCount = int(__count / config.pageSize) + 1
    __pageInfo.pageCount = __pageCount
    __pageInfo.nextPage = int(page) + 1
    __pageInfo.prePage = int(page) - 1
    return render_template('Mainboard/index.html', mainboards=__mainboards, pageInfo=__pageInfo)


@app.route('/Ram/index/<page>', methods=['GET', 'POST'])
def ram(page):
    __ramManager = RamManager()
    __rams = __ramManager.get_rams(page)
    __count = __ramManager.get_ram_count()
    __pageInfo = PageInfo()
    __pageInfo.currentPage = page
    __pageInfo.recordCount = __count
    __pageCount = int(__count / config.pageSize) + 1
    __pageInfo.pageCount = __pageCount
    __pageInfo.nextPage = int(page) + 1
    __pageInfo.prePage = int(page) - 1
    return render_template('Ram/index.html', rams=__rams, pageInfo=__pageInfo)


@app.route('/Hdd/index/<page>', methods=['GET', 'POST'])
def hdd(page):
    __hddManager = HddManager()
    __hdds = __hddManager.get_hdds(page)
    __count = __hddManager.get_hdd_count()
    __pageInfo = PageInfo()
    __pageInfo.currentPage = page
    __pageInfo.recordCount = __count
    __pageCount = int(__count / config.pageSize) + 1
    __pageInfo.pageCount = __pageCount
    __pageInfo.nextPage = int(page) + 1
    __pageInfo.prePage = int(page) - 1
    return render_template('Hdd/index.html', hdds=__hdds, pageInfo=__pageInfo)


@app.route('/Ssd/index/<page>', methods=['GET', 'POST'])
def ssd(page):
    __ssd_manager = SsdManager()
    __ssds = __ssd_manager.get_ssds(page)
    __count = __ssd_manager.get_ssd_count()
    __pageInfo = PageInfo()
    __pageInfo.currentPage = page
    __pageInfo.recordCount = __count
    __pageCount = int(__count / config.pageSize) + 1
    __pageInfo.pageCount = __pageCount
    __pageInfo.nextPage = int(page) + 1
    __pageInfo.prePage = int(page) - 1
    return render_template('Ssd/index.html', ssds=__ssds, pageInfo=__pageInfo)


@app.route('/Graph/index/<page>', methods=['GET', 'POST'])
def graph(page):
    __graph_manager = GraphManager()
    __graphs = __graph_manager.get_graphs(page)
    __count = __graph_manager.get_graph_count()
    __pageInfo = PageInfo()
    __pageInfo.currentPage = page
    __pageInfo.recordCount = __count
    __pageCount = int(__count / config.pageSize) + 1
    __pageInfo.pageCount = __pageCount
    __pageInfo.nextPage = int(page) + 1
    __pageInfo.prePage = int(page) - 1
    return render_template('Graph/index.html', graphs=__graphs, pageInfo=__pageInfo)


@app.route('/Case/index/<page>', methods=['GET', 'POST'])
def case(page):
    __case_manager = CaseManager()
    __cases = __case_manager.get_cases(page)
    __count = __case_manager.get_case_count()
    __pageInfo = PageInfo()
    __pageInfo.currentPage = page
    __pageInfo.recordCount = __count
    __pageCount = int(__count / config.pageSize) + 1
    __pageInfo.pageCount = __pageCount
    __pageInfo.nextPage = int(page) + 1
    __pageInfo.prePage = int(page) - 1
    return render_template('Case/index.html', cases=__cases, pageInfo=__pageInfo)


@app.route('/Power/index/<page>', methods=['GET'])
def power(page):
    power_manager = PowerManager()
    powers = power_manager.get_powers(page)
    count = power_manager.get_power_count()
    pageInfo = PageInfo()
    pageInfo.currentPage = page
    pageInfo.recordCount = count
    pageCount = int(count / config.pageSize) + 1
    pageInfo.pageCount = pageCount
    pageInfo.nextPage = int(page) + 1
    pageInfo.prePage = int(page) - 1
    return render_template('Power/index.html', powers=powers, pageInfo=pageInfo, condition="")


@app.route('/Power/index/<page>', methods=['POST'])
def power_post(page):
    condition = request.form['condition']
    power_manager = PowerManager()
    powers = power_manager.get_powers_by_condition(condition, page)
    count = power_manager.get_power_count_by_condition(condition)
    pageInfo = PageInfo()
    pageInfo.currentPage = page
    pageInfo.recordCount = count
    pageCount = int(count / config.pageSize) + 1
    pageInfo.pageCount = pageCount
    pageInfo.nextPage = int(page) + 1
    pageInfo.prePage = int(page) - 1
    return render_template('Power/index.html', powers=powers, pageInfo=pageInfo, condition=condition)


@app.route('/Power/sync', methods=['GET', 'POST'])
def power_sync():
    __power_manager = PowerManager()
    __power_manager.sync_powers()
    return jsonify(result=True)


if __name__ == '__main__':
    app.run()
