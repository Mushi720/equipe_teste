from pages.CadastroPage import CadastroPage
from hamcrest import assert_that, equal_to

#happy example =)
@given(u'I am on register page')
def step_impl(context):
    context.page_object = CadastroPage(context.driver)
    context.page_object.open_url()

@when(u'I a register a tester')
def step_impl(context):
    context.page_object.register_tester()
    context.page_object.add_user()

@then(u'I must see a success message')
def step_impl(context):
    assert_that(context.page_object.check_result(), equal_to(0))
