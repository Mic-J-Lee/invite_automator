from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Invite
import requests
import json
import os


def extract_username(body):
    target_phrase_index = body.find('Action Notes: Add ')
    index_of_pertinence = target_phrase_index + 18
    end_of_pertinence = body.find(' to GitHub for ')
    pertinent_string = body[index_of_pertinence:end_of_pertinence]
    username = ''
    if pertinent_string[0] == '@':
        username = pertinent_string[1:]
    elif '/' in pertinent_string:
        domain_index = pertinent_string.find('github.com/')
        index_of_username = domain_index + 11
        username = pertinent_string[index_of_username:]
    else:
        username = pertinent_string
    return username

@csrf_exempt
def zapiertogithub(request):
    body = str(request.body)
    if body:
        username = extract_username(body)
    url = ''
    if username:
        url = f'https://api.github.com/orgs/codeplatoon/memberships/{username}'
    github_response_text = requests.put(url, auth=(os.environ['GH_U'], os.environ['GH_T'])).text
    github_response = json.loads(github_response_text)
    invite = Invite()
    if 'state' in github_response:
        if github_response['state'] in ['pending', 'active']:
            invite.successful = True
    if invite.successful == False:
        invite.zapier_payload = body
        invite.github_response = github_response_text
    if username:
        invite.github_handle = username
    invite.save()
    if invite.successful == True:
        return HttpResponse(status=204)
