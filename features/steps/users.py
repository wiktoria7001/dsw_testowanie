from behave import *
import requests
import json

base_url = "https://reqres.in/api"
users = "/users"

headers = {
    'Content-Type': 'application/json'
}


@step('I am in super APP')
def step_impl(context):
    pass


@step('User is created with name:{name} job:{job}')
def step_impl(context, name, job):
    payload = json.dumps({
        "name": name,
        "job": job
    })
    url = base_url + users
    response = requests.request("POST", url, headers=headers, data=payload)
    context.user_id = response.json()['id']


@step('Created user exists in the system')
def step_impl(context):
    url = base_url + users + "/" + context.user_id
    print(url)
    response = requests.request("GET", url, headers=headers, data="")
    print(response)
    assert response.status_code == 200
    context.user_data = response.json()


@step('User {parameter} is {result}')
def step_impl(context, parameter, result):
    assert context.user_data[parameter] == result
