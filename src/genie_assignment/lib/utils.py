__author__ = 'aivaney'

def insert_js_as_var(js_code, var_name, browser):
    """
    Accept variable name, variable value( mostly function expression) and browser object and then insert
    var var_name = js_code value into body element of browser.page_source
    :param js_code str: - js_code function expression
    :param var_name str: - js variable name
    :param browser selenium.webdriver.WebDriver object: - selenium driver object which used to execute script
    :return Boolean: Boolean value to signal whether new js_code inserted correctly
    """
    try:
        browser.execute_script("var script = document.createElement('script');"
                               "script.text = 'var %s=%s';"
                               "document.body.appendChild(script);" % (var_name, js_code))
        return True
    except:
        return False