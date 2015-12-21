import httplib
import json
from gcm import GCM
import sys

GCM_API_KEY = "GVhgVyghvGCYFCDTUHOUDTcHGvgcGHFcvKh876746558Y"  # Your GCM key, you wll get this from your Google Console
LIMIT = 1000  # Sending notification to X devices at a single go

# List of android device registration IDs
registration_ids = []

# Payload of the notification
notification_payload = {
    "action": "BIG_PICTURE",
    "type": "BIG_PICTURE",
    "message": "Your notification message goes here",
    "title": "Your notification title",
    "image_url": "Your image URL goes here",
}

# Function which is used to deliver GCM notifications
def send_notification(registration_ids, notification_payload):
    conn = httplib.HTTPSConnection("android.googleapis.com")
    conn.connect()
    conn.set_debuglevel(1)
    gcm = GCM(GCM_API_KEY)

    global_success = 0
    global_failure = 0
    # print len(registration_ids)

    for i in range(0, len(registration_ids), LIMIT):
        response = gcm.json_request(registration_ids=registration_ids[i:i + LIMIT], data=notification_payload)
        global_success += len(response['success'])
        global_failure += len(response['errors'])

    print "Successfully sent: " + str(global_success)
    print "Failures: " + str(global_failure)

# Calling the function here
send_notification(registration_ids, notification_payload)
