import pywhatkit
def send_whatsapp_message(phone_number, message, time_hour, time_minute):
    """
    Sends a WhatsApp message to a specified phone number at a specified time.

    :param phone_number: str, the phone number in the format '+1234567890'
    :param message: str, the message to send
    :param time_hour: int, the hour at which to send the message (24-hour format)
    :param time_minute: int, the minute at which to send the message
    """
    pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute)
if __name__ == "__main__":
    phone_number = input("Enter the phone number (with country code): ")
    message = input("Enter the message to send: ")
    time_hour = int(input("Enter the hour to send the message (24-hour format): "))
    time_minute = int(input("Enter the minute to send the message: "))
    
    send_whatsapp_message(phone_number, message, time_hour, time_minute)
    print("Message scheduled successfully!")