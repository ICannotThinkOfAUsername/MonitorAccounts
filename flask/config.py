setup_config #Comment this line out after setting up config

#Necessary
pa_username = '' #Your PythonAnywhere username
db_password = '' #Your MySQL password
webhook_url = '' #Your discord webhook url

#Optional
expire_after = 5 #The monitoring script will consider accounts inactive after [expire_after] seconds have passed since their more recent /alive/ update
check_every = 10 #The monitoring script will check for inactive accounts every [check_every] seconds