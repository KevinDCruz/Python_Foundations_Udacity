from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACda7645742cd075eac3dcc97efc3e87d8"
# Your Auth Token from twilio.com/console
auth_token  = "8a9f88b4db9b44032b63189ee4d67bd1"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+17744888884", #Destination_number
    from_="+15083869348", #Twilio Number
    body="I know what you did last weekend")

print(message.sid)