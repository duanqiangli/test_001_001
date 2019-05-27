import pytest,allure

class Test001:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="步骤描述")
    def test_001(self):
        allure.attach("步骤","步骤1")
        print("test_001")
        assert True




