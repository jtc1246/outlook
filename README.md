# Outlook v1.0.1

## 1. Introduction

Microsoft does not open any API to ordinary users. It only opens an API access to software developers, and these developers can make their software connect to microsoft service. For example, if you can send an Outlook email in a third-party app, then this app uses this API access. As a result, if we just want to send some emails ourselves, it's very difficult to complete the API access, so I wrote this program to make these things simpler.


## 2. Functions

You only need to login once when you first use this program. After that, you can send emails with it directly. The login status will be valid in 2 to 3 months. But you can only log in one account at the same time, and if you log in another account, the previous one will be invaild. This program will store the account information in a file on your device. In a few devices, the program may not have the permission to write or read this file, so you need to log in every time. Note that this program can only send emails and cannot receive emails, for the safety.


## 3. Usage

### (1) Log in

You can use setAccount() to log in. When you run setAccount(), it will give you an url, you need to copy it and open it in your browser, log in your account, and then copy the url afterwards including "localhost", it's normal that your browser shows "This site can't be reached". Paste this to python, then the account will be added successfully. The login status will be valid for 2 to 3 months. This means that if you use this next time, you needn't log in again. But if you use another account on same device or delete the file storing account information, the login status will become invalid.

### (2) Send an email

You need to have a login status when sending emails. Then use the following function:

sendEmail(subject:str,content:str,receiver:str)

Subject is the title of your email, receiver is the email address that you want to send this email to.

Return value: int

    0: success
    -9: invalid account / no account
    -1 ~ -4: same to myHttp  https://github.com/jtc1246/myHttp


## 4. Safety

① Can I get your password or send email with your account?

No. Your account information is only stored in your device and these information will only be given to microsoft. Your information will not be uploaded to any other server.

② Can other people or other software get your password or send email with your account?

Others can never get your password, because after logged in, microsoft will use another method to authenticate and password is not used any more, the password will not be stored in your device. However, other people or other software can read the file storing your account information, which means that they can send email with your account.

③ Why cannot this program receive email?

For the safety. Other people or software can read the file storing your account information. If allowing receiving emails, it's very dangerous.


## 5. Others

    Installation: pip3 install outlook
    Email: jtc1246@outlook.com
    LICENSE: GPL v2
    Requirement: Python 3

