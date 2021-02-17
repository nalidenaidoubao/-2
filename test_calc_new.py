import allure
import pytest


# 文件名以test_开头， 类名以Test开头， 方法名以test_开头
# 注意：测试类里一定不要加__init__()方法
@allure.feature("测试计算器")
class TestCalc:
    '''
    优化点
    1，把setup和teardown换为了fixture方法
    2，把get_calc放到了conftest的文件中
    3，把参数化换为了 fixture参数化方式
    4，测试用例中的数据需要通过 get_datas获取
    get_datas 返回了列表
    '''

    @allure.story("测试加法")
    @pytest.mark.add
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_datasadd):
        # 实例化计算器类
        # calc = Calculator()
        # 定义一个变量接收add方法的返回值
        # 调用相加方法
        with allure.step("计算两数的相加和"):
            result = get_calc.add(get_datasadd[0], get_datasadd[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == get_datasadd[2]

    @allure.story("测试除法")
    @pytest.mark.div  # 标记为除法
    @pytest.mark.run(order=2)
    def test_div(self, get_calc, get_datasdiv):
        with allure.step("计算两数的除法"):
            result = get_calc.div(get_datasdiv[0], get_datasdiv[1])
        if isinstance(result, float):
            result = round(result, 1)
            result = int(result)
        assert result == get_datasdiv[2]

    @allure.story("测试减法")
    @pytest.mark.sub  # 标记为减法
    @pytest.mark.run(order=3)
    def test_sub(self, get_calc, get_datassub):
        with allure.step("计算两数的减法"):
            result = get_calc.sub(get_datassub[0], get_datassub[1])
        if isinstance(result, float):
            result = round(result, 1)
            result = int(result)
        assert result == get_datassub[2]

    @allure.story("测试乘法")
    @pytest.mark.sub  # 标记为减法
    @pytest.mark.run(order=4)
    def test_mul(self, get_calc, get_datasmul):
        with allure.step("计算两数的减法"):
            result = get_calc.mul(get_datasmul[0], get_datasmul[1])
        if isinstance(result, float):
            result = round(result, 1)
            result = int(result)
        assert result == get_datasmul[2]
