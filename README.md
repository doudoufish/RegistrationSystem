# RegistrationSystem
## Directory structure
<img width="500" alt="image" src="https://user-images.githubusercontent.com/96038218/182024410-aa769db4-a87a-49db-893d-9c541be97280.png">

## Step1: create regist.html
* If the user clicks Start Registering, this URL will be activated from the client:
* http://localhost:8000/cgi-bin/regist.py

## Step2: setup regist.py
* For this part, let the customer edit their name and email.
* When they click submit, the server will force customre to the process.py
* http://localhost:8000/cgi-bin/process.py?name=<name>mail=<mail>

## Step3: process.py
* In this page, it is use to conform the registraction from correct or not.
* Onece customer click submit, the server will sent you to the confirm.py
* http://localhost:8000/cgi-bin/confirm.py?confirm=(YES or NO)

## Step4: confim.py
* In the confrim page, It will shows the registraction result.
* When the customer choose YES in last step, it will shows Successful page.
* When the customer choose No in last step, the server will stell you information is incorrect, and let you registraction agin or go to top.

## Step5: PPT
https://docs.google.com/presentation/d/1rvB5G8sTF3fEyzeI6yMxGAv1hzFMs_AzT6vY6ILfz-Y/edit?usp=sharing
