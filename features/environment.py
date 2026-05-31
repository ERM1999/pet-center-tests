from utils.browser import create_browser

def before_all(context):
    context.driver = create_browser()

def after_all(context):
    context.driver.quit()
