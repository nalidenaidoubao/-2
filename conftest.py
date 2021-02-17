import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add']
    add_datas = add_datas['datas']
    div_datas = datas['div']
    div_datas = div_datas['datas']
    sub_datas = datas['sub']
    sub_datas = sub_datas['datas']
    mul_datas = datas['mul']
    mul_datas = mul_datas['datas']


@pytest.fixture(params=add_datas)
def get_datasadd(request):
    print('开始计算')
    data = request.param
    print(f'测试数据为{data}')
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas)
def get_datasdiv(request):
    print("开始计算")
    data = request.param
    print(f'c测试数据为{data}')
    yield data
    print("计算结束")


@pytest.fixture(params=sub_datas)
def get_datassub(request):
    print("开始计算")
    data = request.param
    print(f'c测试数据为{data}')
    yield data
    print("计算结束")


@pytest.fixture(params=mul_datas)
def get_datasmul(request):
    print("开始计算")
    data = request.param
    print(f'c测试数据为{data}')
    yield data
    print("计算结束")