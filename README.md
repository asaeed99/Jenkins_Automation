# Jenkins_Automation

## Run automated script in python using the following command:

!!! Note
    * Please adjust paths and parameters accordingly

```/Users/I545311/.pyenv/versions/3.7.8/bin/python /Users/I545311/Documents/GitHub/i545311/Jenkins_Job_Automation/email_automation.py  --smtp_server_name <smpt.server.com> --smtp_server_port <port number> --sender_email <no-reply-sre@test.com> --receiver_emails <John.smith@test.com,rodger.more@test.com> --email_body <Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET> --sender_pass <xxxxxxxxxxxxxxxx>```


## Run automated script via Jenkins pipeline using the following guide


1. In Jenkins page go to new item and create ```Freestyle project```
2. In Configure go to Source code management and choose ```GIT```. In repo URL provide ```https://github.tools.sap/I545311/Jenkins_Job_Automation.git``` and your credentials
3. In Branch specifier ```*/main```
4. To run Jenkins build on every Saturday choose ```Build periodically``` and add the following command ```* * * * 6```
5. Then go to Build steps and choose ```Execute shell``` and provide the following command

!!! Note
    * Please adjust paths and parameters accordingly

```python3 email_automation.py  --smtp_server_name <smpt.server.com> --smtp_server_port <port number> --sender_email <no-reply-sre@test.com> --receiver_emails <John.smith@test.com,rodger.more@test.com> --email_body <"Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET"> --sender_pass <xxxxxxxxxxxxxxxx>```
