from requests import get, post, delete, put
import os

os.system("git restore ../db/mars_explorer.db")
print("Get all jobs:",
      "pass" if
      str(get("http://127.0.0.1:5000/api/v2/jobs").json()) ==
      "{'jobs': [{'collaborators': '2, 3', 'end_date': None, 'id': 1, 'is_finished': False, 'job': 'j1', 'start_date': None, 'team_leader': 1, 'work_size': 1}, {'collaborators': '3, 4', 'end_date': None, 'id': 2, 'is_finished': True, 'job': 'j2', 'start_date': None, 'team_leader': 2, 'work_size': 2}, {'collaborators': '4, 5', 'end_date': None, 'id': 3, 'is_finished': False, 'job': 'j3', 'start_date': None, 'team_leader': 3, 'work_size': 3}, {'collaborators': '5, 6', 'end_date': None, 'id': 4, 'is_finished': True, 'job': 'j4', 'start_date': None, 'team_leader': 4, 'work_size': 4}, {'collaborators': '6, 7', 'end_date': None, 'id': 5, 'is_finished': False, 'job': 'j5', 'start_date': None, 'team_leader': 5, 'work_size': 5}, {'collaborators': '7, 8', 'end_date': None, 'id': 6, 'is_finished': True, 'job': 'j6', 'start_date': None, 'team_leader': 6, 'work_size': 6}, {'collaborators': '8, 9', 'end_date': None, 'id': 7, 'is_finished': False, 'job': 'j7', 'start_date': None, 'team_leader': 7, 'work_size': 7}, {'collaborators': '9, 10', 'end_date': None, 'id': 8, 'is_finished': True, 'job': 'j8', 'start_date': None, 'team_leader': 8, 'work_size': 8}, {'collaborators': '10, 1', 'end_date': None, 'id': 9, 'is_finished': False, 'job': 'j9', 'start_date': None, 'team_leader': 9, 'work_size': 9}, {'collaborators': '1, 2', 'end_date': None, 'id': 10, 'is_finished': True, 'job': 'j10', 'start_date': None, 'team_leader': 10, 'work_size': 10}]}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Get one job:",
      "pass" if
      str(get("http://127.0.0.1:5000/api/v2/jobs/2").json()) ==
      "{'job': {'collaborators': '3, 4', 'end_date': None, 'id': 2, 'is_finished': True, 'job': 'j2', 'start_date': None, 'team_leader': 2, 'work_size': 2}}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Get one job that not exist:",
      "pass" if
      str(get("http://127.0.0.1:5000/api/v2/jobs/11").json()) ==
      "{'message': 'Job 11 not found'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Delete job (Need 'Get one job' to pass):",
      "pass" if
      str(delete("http://127.0.0.1:5000/api/v2/jobs/1").json()) ==
      "{'success': 'OK'}" and
      str(get("http://127.0.0.1:5000/api/v2/jobs/1").json()) ==
      "{'message': 'Job 1 not found'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Delete job that not exist:",
      "pass" if
      str(delete("http://127.0.0.1:5000/api/v2/jobs/11").json()) ==
      "{'message': 'Job 11 not found'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Add new job:",
      "pass" if
      str(post("http://127.0.0.1:5000/api/v2/jobs", json={'collaborators': '3, 4', 'end_date': None, 'is_finished': True, 'job': 'j2', 'start_date': None, 'team_leader': 2, 'work_size': 2}).json()) == 
      "{'success': 'OK'}"
      and 
      str(get("http://127.0.0.1:5000/api/v2/jobs/11").json()) ==
      "{'job': {'collaborators': '3, 4', 'end_date': None, 'id': 11, 'is_finished': True, 'job': 'j2', 'start_date': None, 'team_leader': 2, 'work_size': 2}}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Edit job (need Get one job to pass):",
      "pass" if
      str(put("http://127.0.0.1:5000/api/v2/jobs/1", json={'job': 'j11'}).json()) ==
      "{'success': 'OK'}"
      and
      str(get("http://127.0.0.1:5000/api/v2/jobs/1").json()) ==
      "{'job': {'collaborators': '2, 3', 'end_date': None, 'id': 1, 'is_finished': False, 'job': 'j11', 'start_date': None, 'team_leader': 1, 'work_size': 1}}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Edit job that not exist:",
      "pass" if
      str(put("http://127.0.0.1:5000/api/v2/jobs/11", json={'job': 'j11'}).json()) ==
      "{'message': 'Job 11 not found'}"
      else "fail")
