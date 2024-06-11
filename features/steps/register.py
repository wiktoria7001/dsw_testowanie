from behave import *
import requests
import json

base_url = "https://reqres.in/api"
register = "/register"

headers = {
    'Content-Type': 'application/json'
}


@step('I sign in super APP')
def step_impl(context):
    pass


@step('User is registered with email:{email} password:{password}')
def step_impl(context, email, password):
    payload = json.dumps({
        "email": email,
        "password": password
    })
    url = base_url + register
    response = requests.request("POST", url, headers=headers, data=payload)
    context.response_data = response.json()
    context.status_code = response.status_code


@step('Registration is successful')
def step_impl(context):
    assert context.status_code == 200, f"Expected status code 200 but got {context.status_code}"


@step('User token is not empty')
def step_impl(context):
    assert 'token' in context.response_data, "Token not found in response"
    assert context.response_data['token'], "Token is empty"
