# Python-Android-GCM
A python script to send GCM notifications for Android devices

#### Step One - Set Up Python GCM Simple Server
Log in to your server with a sudo user.

* Update your package lists:

```shell
sudo apt-get update
```

* Install the Python packages:

```shell
sudo apt-get install python-pip python-dev build-essential
```

* Install python-gcm. Find out more about python-gcm here.

```shell
sudo pip install python-gcm
```

#### Explanation:

<code>from gcm import *</code>: this imports the Python client for Google Cloud Messaging for Android

<code>gcm</code>: add your API KEY from the Google API project; make sure your server's IP address is in the allowed IPs

<code>registration_ids</code>: add registration_ids of your Android devices to whom you would like to send notifications
