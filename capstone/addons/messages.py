""" Twilio Login
# Username: instructor@pdxcodeguild.com
# Password: Codeguild123
# Auth Token: 1769e4656916ec050cdbe4e58d17e6c1
# Acct SID: AC86189c370a1fcca6c3dd11c2fa15ee04 """




SMS_MESSAGES = {
    'IN': "Hello {b1_first_name}, My name is {loan_processor} and I am assisting {loan_officer} with your Equity loan.  "
          "Feel free to email at email@email.com with any questions, or call 555-555-5555.  Have a great day!",
    'PR': "Hello {b1_first_name}, I have submitted your file for review. Have a great day!",
    'IA': "Hello {b1_first_name}, Your file has been initial approved by underwriting. "
          "Please let me know if you have questions.",
    'FN': "Hi {b1_first_name}, Your loan has been final approved!.",
}


EMAIL_MESSAGES = {
    'IN': "Hello {0}, My name is {1} and I am assisting {2} with your Equity loan.",
    'PR': "Hello {0}, I have submitted your file for review. Have a great day!",
    'IA': "Hello {0}, Your file has been initial approved by underwriting. Please let me know if you have questions.",
    'FN': "Hi {0}, Your loan has been final approved!.",
}