from twilio import rest

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+17744888884", #Destination_number
    from_="+15083869348", #Twilio Number
    body="I know what you did last weekend")

print(message.sid)