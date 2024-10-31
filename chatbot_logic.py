from fuzzywuzzy import process
import random

# Define your keywords and responses
responses = {
    "branch": [
        "Our college offers branches in CSE, AIML, IOT, DS, IT, MECH, CIVIL, ECE, and EEE. Let me know if you need more details!",
        "Sure! We have various branches: CSE, AIML, IOT, DS, IT, MECH, CIVIL, ECE, and EEE."
    ],
    "fee": [
        "The fee structure varies by branch and scholarship status. You can visit our website for more details.",
        "Fees depend on the branch and any scholarships you might have. Check our website for specifics!"
    ],
    "location": [
        "Our college is located in Malakpet, Hyderabad, Telangana. It's a great place to study!",
        "We are situated in Malakpet, Hyderabad, Telangana. Feel free to ask if you want directions!"
    ],
    "faculty": [
        "Our faculty includes experienced professors and industry experts who are here to support your learning.",
        "We have a wonderful faculty with industry experience and academic expertise."
    ],
    "placement": [
        "Our placement record is strong, with companies like TCS, Infosys, and Wipro actively recruiting our graduates.",
        "We take pride in our placement opportunities, partnering with leading companies like TCS, Infosys, and Wipro."
    ],
    "student activities": [
        "We offer a variety of student activities, including tech, arts, sports, and entrepreneurship clubs. Join us!",
        "You can participate in numerous student activities, from tech to arts and sports!"
    ]
}

def get_response(user_input):
    user_input = user_input.lower()

    # Use fuzzy matching to find the closest match
    keywords = list(responses.keys())
    matched_keyword, confidence = process.extractOne(user_input, keywords)

    # Set a confidence threshold (e.g., 60)
    if confidence >= 60:
        # Choose a random response from the matched keyword's list
        return random.choice(responses[matched_keyword])
    else:
        return random.choice([
            "I'm here to help! You can ask me about branches, fees, location, faculty, placements, and student activities.",
            "I’m glad you’re asking! Feel free to inquire about our branches, fees, location, faculty, placements, or student activities.",
            "I'm here to assist you! What would you like to know about? Our branches, fees, location, faculty, placements, or student activities?"
        ])