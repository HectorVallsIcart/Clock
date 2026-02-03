def clock(num):
    # Split the input string "HH:MM:SS"
    hour_text, minute_text, second_text = num.split(":")

    # Convert each part to integer
    hour = int(hour_text)
    minute = int(minute_text)
    second = int(second_text)

    # Determine message based on time range
    if 1 <= hour < 8:
        sms = "It's still time to sleep"
    elif 8 <= hour < 14:
        sms = "Good morning"
    elif 14 <= hour < 21:
        sms = "Good afternoon"
    else:
        sms = "Good night"

    return {
        "hour": hour,
        "minute": minute,
        "second": second,
        "sms": sms,
        "text": f"It is {hour}:{minute}:{second}"
    }
