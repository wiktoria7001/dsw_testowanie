from behave import *
import requests
import json

base_url = "https://reqres.in/api"
login_endpoint = "/login"

headers = {
    'Content-Type': 'application/json'
}


@step('I log in super APP')
def step_impl(context):
    pass


@step('User logs in with email:{email} password:{password}')
def step_impl(context, email, password):
    payload = json.dumps({
        "email": email,
        "password": password
    })
    url = base_url + login_endpoint
    response = requests.request("POST", url, headers=headers, data=payload)
    context.login_response = response


@step('User is successfully logged in')
def step_impl(context):
    assert context.login_response.status_code == 200
    context.login_data = context.login_response.json()


@step('Login token is returned')
def step_impl(context):
    assert 'token' in context.login_data
