from datetime import datetime

def generate_datetime_string():
    return datetime.now().strftime("%Y%m%d_%H%M%S")