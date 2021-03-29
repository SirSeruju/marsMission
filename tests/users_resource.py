from requests import get, post, delete, put
import os

os.system("git restore ../db/mars_explorer.db")
print("Get all users:",
      "pass" if
      str(get("http://127.0.0.1:5000/api/v2/users").json()) ==
      """{'users': [{'address': 'a1', 'age': 1, 'email': 'e1@e1.e1', 'id': 1, 'modified_date': None, 'name': 'n1', 'position': 'p1', 'speciality': 'sp1', 'surname': 's1'}, {'address': 'a2', 'age': 2, 'email': 'e2@e2.e2', 'id': 2, 'modified_date': None, 'name': 'n2', 'position': 'p2', 'speciality': 'sp2', 'surname': 's2'}, {'address': 'a3', 'age': 3, 'email': 'e3@e3.e3', 'id': 3, 'modified_date': None, 'name': 'n3', 'position': 'p3', 'speciality': 'sp3', 'surname': 's3'}, {'address': 'a4', 'age': 4, 'email': 'e4@e4.e4', 'id': 4, 'modified_date': None, 'name': 'n4', 'position': 'p4', 'speciality': 'sp4', 'surname': 's4'}, {'address': 'a5', 'age': 5, 'email': 'e5@e5.e5', 'id': 5, 'modified_date': None, 'name': 'n5', 'position': 'p5', 'speciality': 'sp5', 'surname': 's5'}, {'address': 'a6', 'age': 6, 'email': 'e6@e6.e6', 'id': 6, 'modified_date': None, 'name': 'n6', 'position': 'p6', 'speciality': 'sp6', 'surname': 's6'}, {'address': 'a7', 'age': 7, 'email': 'e7@e7.e7', 'id': 7, 'modified_date': None, 'name': 'n7', 'position': 'p7', 'speciality': 'sp7', 'surname': 's7'}, {'address': 'a8', 'age': 8, 'email': 'e8@e8.e8', 'id': 8, 'modified_date': None, 'name': 'n8', 'position': 'p8', 'speciality': 'sp8', 'surname': 's8'}, {'address': 'a9', 'age': 9, 'email': 'e9@e9.e9', 'id': 9, 'modified_date': None, 'name': 'n9', 'position': 'p9', 'speciality': 'sp9', 'surname': 's9'}, {'address': 'a10', 'age': 10, 'email': 'e10@e10.e10', 'id': 10, 'modified_date': None, 'name': 'n10', 'position': 'p10', 'speciality': 'sp10', 'surname': 's10'}]}"""
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Get one user:",
      "pass" if
      str(get("http://127.0.0.1:5000/api/v2/users/1").json()) ==
      "{'user': {'address': 'a1', 'age': 1, 'email': 'e1@e1.e1', 'id': 1, 'modified_date': None, 'name': 'n1', 'position': 'p1', 'speciality': 'sp1', 'surname': 's1'}}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Get one user that not exist:",
      "pass" if
      str(get("http://127.0.0.1:5000/api/v2/users/11").json()) ==
      "{'message': 'User 11 not found'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Delete user (Need 'Get one user' to pass):",
      "pass" if
      str(delete("http://127.0.0.1:5000/api/v2/users/1").json()) ==
      "{'success': 'OK'}" and
      str(get("http://127.0.0.1:5000/api/v2/users/1").json()) ==
      "{'message': 'User 1 not found'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Delete user that not exist:",
      "pass" if
      str(delete("http://127.0.0.1:5000/api/v2/users/11").json()) ==
      "{'message': 'User 11 not found'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Add new user:",
      "pass" if
      str(post("http://127.0.0.1:5000/api/v2/users", json={'address': 'a11', 'age': 11, 'email': 'e11@e11.e11', 'name': 'n11', 'position': 'p11', 'speciality': 'sp11', 'surname': 's11', 'hashed_password': 'p11'}).json()) ==
      "{'success': 'OK'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Add new user with existing email:",
      "pass" if
      str(post("http://127.0.0.1:5000/api/v2/users", json={'address': 'a11', 'age': 11, 'email': 'e1@e1.e1', 'name': 'n11', 'position': 'p11', 'speciality': 'sp11', 'surname': 's11', 'hashed_password': 'p11'}).json()) ==
      "{'message': 'Email e1@e1.e1 already exist'}"
      else "fail")

os.system("git restore ../db/mars_explorer.db")
print("Edit user (need 'Get one user to pass'):",
      "pass" if
      str(put("http://127.0.0.1:5000/api/v2/users/1", json={'address': 'a11'}).json()) ==
      "{'success': 'OK'}"
      and
      str(get("http://127.0.0.1:5000/api/v2/users/1").json()) != 
      "{'user': {'address': 'a1', 'age': 1, 'email': 'e1@e1.e1', 'id': 1, 'modified_date': None, 'name': 'n1', 'position': 'p1', 'speciality': 'sp1', 'surname': 's1'}}"
      else "fail")

