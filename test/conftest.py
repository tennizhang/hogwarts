# import pytest
import os
import datetime
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
def pytest_configure(config):
    time_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    config.option.log_file = os.path.join(config.rootdir, 'logs', f'{time_now}.log')
#
# # 配置log文件名称
# @pytest.fixture(scope="session", autouse=True)
# def manage_logs(request):
#     """Set log file name same as test name"""
#     now = time.strftime("%Y-%m-%d_%H-%M-%S")
#     log_name = '.logs/' + now + '.logs'
#     request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(return_path(log_name))