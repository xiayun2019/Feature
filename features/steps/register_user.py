#coding = utf-8
from behave import *
#使用正则表达式
use_step_matcher('re')

@when('I open the website by url "([^"]*)"')
def step_open_brower(context,url):
    context.driver.get(url)

@then('I find the title is "([^"]*)"')
def step_is_title(context,title):
    _title = context.driver.title
    assert title in _title