from data import get_data
from messenger import send_message

if __name__ == "__main__":

    data = get_data() # Get Covid-19 Data

    send_message(data) # Send out text