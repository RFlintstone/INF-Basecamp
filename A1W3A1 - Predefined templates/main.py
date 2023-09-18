# Usually companies use a predefined templates in their emails. A company named XYZ would like to have a Python
# program that collects basic information and generates the content of the email.
#
# Criteria: - There are only two templates: Job Offer and Rejection. - For the Job Offer email, the program asks:
# first name, last name, job title, annual salary, starting date. - For the Rejection email, the program asks: first
# name, last name, job title, with or without feedback, one feedback statement in case it is with feedback. - The
# program must check valid input formats: - First and last names: each minimum two characters and maximum ten
# characters; containing only alphabets, both starting with capital letters. - Job title: minimum 10 characters
# without numbers. - Salary: valid floating point number between (and including) 20.000,00 and 80.000,00. - Date:
# only in YYYY-MM-DD format, no negative numbers, days between 1 - 31, month between 1 - 12, year only 2021 and 2022.
# - Feedback: if the email contains a feedback there is an extra line in the text otherwise that line must be
# removed. - The program will generate emails until the user answers No to the More Letters? question. - In case of
# invalid input from the user, the program must print the message Input error and then repeat the question again.
#
# https://app.codegra.de/courses/5199/assignments/38791/submissions#description

# Prepare the email though this method.
def prepare_email(email_properties):
    # Check if it's a job offer.
    if email_properties[0].lower() == "job offer" or email_properties[0].lower() == "jo":
        # Get input and add it to the email properties array (list)
        anual_salary = input("")
        email_properties.append(anual_salary)
        starting_date = input("")
        email_properties.append(starting_date)

        # date_split = starting_date.split("-")

        # Check if we have a correct anual salary in the correct range
        if float(anual_salary.replace(",", "").replace(".", "")) < float(20000) or float(
                anual_salary.replace(",", "").replace(".", "")) > float(80000):
            print("Input error")

        # if date_split[0] not in range(2021, 2022) and date_split[1] not in range(1, 31) and date_split[2] not in
        # range(1, 12): print("Input error - DATE NOT IN RANGE")

    # Check if the email type is a rejection
    elif email_properties[0].lower() == "rejection" or email_properties[0].lower() == "rej":
        # Ask for user input and add the feedback the the email properties array (list)
        with_feedback = input("")
        email_properties.append(with_feedback)

        # Check if the user wants feedback
        if with_feedback.lower() == "yes":
            # Ask for feedback if the answer is yes and add the feedback to the array (list)
            feedback = input("")
            email_properties.append(feedback)

    # Return all our changed email properties list
    return email_properties


# Make the email
def send_email(email_properties):
    # Begin the email and add the first text
    mail = ""
    mail += (f'Dear {email_properties[1]} {email_properties[2]},\nAfter careful evaluation of your application for the '
             f'position of {email_properties[3]},\n')

    # If the email type is a job offer we should have different text then when we want to reject someone
    if email_properties[0].lower() == "job offer" or email_properties[0].lower() == "jo":
        mail += (f'we are glad to offer you the job. Your salary will be {str(email_properties[4])} euro annually. \n'
                 f'Your start date will be on {email_properties[5]}. Please do not hesitate to contact us with any '
                 f'questions.')

    # If the email type is a rejection we should have different text then when we want to hire someone
    elif email_properties[0].lower() == "rejection" or email_properties[0].lower() == "rej":
        mail += 'at this moment we have decided to proceed with another candidate.\n'
        # Check if we wanted to provide feedback, and then send the provided feedback with the email.
        if email_properties[4].lower() == "yes":
            mail += ('Here we would like to provide you our feedback about the interview.\n' + f'{email_properties[5]}')
        mail += ('We wish you the best in finding your future desired career. Please do not hesitate to contact us '
                 'with any questions.')

    # End the email
    mail += "\nSincerely,\nHR Department of XYZ"

    print("Here is the final letter to send:")

    # Return the email so we can call it outside of the function
    return mail


def main():
    # Do we want more letters?
    more_letters = input("")

    # If we want more letters, ask for the details of the new letter
    if more_letters or more_letters.lower() == "yes":
        # Ask for user input
        email_type = input("")
        first_name = input("")
        last_name = input("")
        job_title = input("")

        # If the length of first_name if less then 2 or more then 10, print error.
        if len(first_name) < 2 or len(first_name) > 10:
            print("Input error")
        # If the length of last_name if less then 2 or more then 10, print error.
        elif len(last_name) < 2 or len(last_name) > 10:
            print("Input error")
        # If the length of job_title is less then 10, print error.
        elif len(job_title) < 10:
            print("Input error")
        # If we have a digit in job_title, print error.
        elif any(chr.isdecimal() for chr in job_title):
            print("Input error")
        # If we don't have any errors, proceed.
        else:
            email_properties = prepare_email([email_type, first_name, last_name, job_title])
            email = send_email(email_properties)
            print(email)


# Run the script.
main()