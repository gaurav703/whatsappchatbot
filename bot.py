from dateutil.parser import parse
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from RoboHashpy import RoboHash


app = Flask(__name__)
count = 0

@app.route("/sms", methods=['POST'])

def reply():
    global c, d
    incoming_msg = request.form.get('Body').lower()
    response = MessagingResponse()
    message = response.message()
    words = incoming_msg.split('@')
    responded = False
    if "hello" in incoming_msg:
        start = "Hello! \nDo you want to set a meeting timing?"
        message.body(start)
        responded = True

    if len(words) == 1 and "yes" in incoming_msg:
        reminder_string = "Please provide time in the following format only.\n\n" \
                          "*Time @* _type the time_ "
        message.body(reminder_string)
        responded = True

    if len(words) == 1 and "no" in incoming_msg:
        REPLY = "Ok. Have a nice day!"
        message.body(REPLY)
        responded = True

    elif len(words) != 1:
        input_type = words[0].strip().lower()
        input_string = words[1].strip()

        if input_type == "time":
            REPLY = "Please enter the meeting message in the following format only.\n\n" \
                    "*Reminder @* _type the message_"
            c = date(input_string)
            message.body(REPLY)
            responded = True

        if input_type == "reminder":
            d = reminder(input_string)
            message.body("Hello Everyone!\n"+"Meet time : "+c+"\nMeet purpose:"+d)
            responded = True

        """if "image" in incoming_msg:
            REPLY = "Please enter the image name in the following format only.\n" \
                    "*Image @* _type the image name_"
            message.body(REPLY)
            responded = True"""

        if input_type == "image":
            img = image(input_string)
            rb = RoboHash()
            message.media(rb.get_im_hash(img,1))
            responded = True
        if input_type == "reason":
            imp = important(input_string)
            message.body(imp)
            responded = True

    if "link" in incoming_msg:
        message.body('https://meet.google.com/sei-cffs-zgr?pli=1')
        responded = True

    if not responded:
        message.body('Incorrect request format. Please enter in the correct format')

    return str(response)


def date(msg):
    t = parse(msg)
    time = t.strftime('%H:%M')
    return time


def reminder(msg):
    return msg

def image(msg):
    return msg

def important(msg):
    return msg

if __name__ == "__main__":
    app.run(debug=True)

