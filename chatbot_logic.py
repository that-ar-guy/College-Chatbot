# chatbot.py
def get_response(user_input):
    user_input = user_input.lower()

    if "branch" in user_input:
        return "Our college offers branches in CSE, AIML, ECE, ME, etc."
    elif "fee" in user_input:
        return "The fee structure varies by branch and scholarship status. Visit our website for more details."
    elif "location" in user_input:
        return "Our college is located at Hyderabad, Telangana."
    elif "faculty" in user_input:
        return "Our faculty includes experienced professors and industry experts."
    elif "placement" in user_input:
        return "Our placement record is strong, with companies like TCS, Infosys, and Wipro recruiting."
    elif "student activities" in user_input:
        return "We offer student activities, including tech, arts, sports, and entrepreneurship clubs."
    else:
        return "I'm here to answer questions about branches, fees, location, faculty, placements, and student activities. Please ask about one of these topics."
