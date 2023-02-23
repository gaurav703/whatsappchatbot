# whatsappchatbot

Working:
 This Chatbot is made in Python, Flask, Ngrok for local hosting and Twilio WhatsApp sandbox. It
take time and purpose of meeting from user as an input and gave us a default set message which
will we send in an group and link of google meet for meeting.


Flask:
 I then wrapped the bot in a simple Flask webapp using a POST method. Flask is a simple micro
web framework that allows you to create web apps using Python. Basically, if you look at the python
file in the github link below, you will see that I just set up a function that listens for incoming
messages via the POST method and reply as written in message response object. 

![Screenshot 2023-02-23 212556](https://user-images.githubusercontent.com/111629507/220960969-dafc4ea2-e6cb-444c-973f-85422070f83b.png)
![Screenshot 2023-02-23 212939](https://user-images.githubusercontent.com/111629507/220961786-6a415c94-cf62-4276-82ad-f92799a69141.png)

Ngrok:
 After that , I used Ngrok to expose the appropriate port that the web app was running on my
local PC to the internet. Ngrok creates a url that connects your web app to the external web.
 Twilio:
 Twilio is a service that allows you to programmatically (i.e through code) set how your
applications work with communication channels like regular phone lines, sms or even Whatsapp.
Once you set up a Programmable Messaging project in Twilio, it registers a number that you can
exchange messages with in Whatsapp. You then use the URL from Ngrok to connect to the Twilio
Whatsapp Console. After that , once you register your mobile # with the Whatsapp account using an
initialisation code , whenever you send any further messages to the Whatsapp account , Twilio will
pass that message to the Python Flask WebApp and receive & display any responses that come back
 
 
 
