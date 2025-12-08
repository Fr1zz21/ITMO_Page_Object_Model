from pages.swag_labs import SwagLabs


def test_check_icon(driver):
    tests = SwagLabs(driver)
    tests.visit()
    assert tests.exist_icon()
    
def test_find_username_field(driver):
    tests = SwagLabs(driver)   
    tests.username_field()

def test_find_password_field(driver):
    tests = SwagLabs(driver)
    tests.password_field()


