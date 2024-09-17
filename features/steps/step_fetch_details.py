import requests
from behave import *

from features.steps.endpoints import API_ENDPOINT, add_query_param


@given('the user with id {user_id}')
def step_impl(context, user_id):
    context.url = API_ENDPOINT + "/" + user_id
    #print(context.url)

@when('sent request user')
def step_impl(context):
    context.response = requests.get(context.url)
    print(context.response.content)

@then('should return status code {expected_status_code}')
def step_impl(context, expected_status_code):
    code = context.response.status_code
    print("Status code: ", code)
    assert code == int(expected_status_code), f"Not Matched, please verify..."

@given('the user with following genders')
def step_impl(context):
    for row in context.table:
        gender = row['gender']
        print("Current gender: ", gender)
        #print(add_query_param("","","",gender))
        context.url = API_ENDPOINT + add_query_param("","","",gender)
        #print(context.url)

