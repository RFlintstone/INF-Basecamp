# Usually companies use a predefined templates in their emails.
# A company named XYZ would like to have a Python program that collects basic information and generates the content of the email.
#
# Criteria:
# - There are only two templates: Job Offer and Rejection.
# - For the Job Offer email, the program asks: first name, last name, job title, annual salary, starting date.
# - For the Rejection email, the program asks: first name, last name, job title, with or without feedback, one feedback statement in case it is with feedback.
# - The program must check valid input formats:
#   - First and last names: each minimum two characters and maximum ten characters; containing only alphabets, both starting with capital letters.
#   - Job title: minimum 10 characters without numbers.
#   - Salary: valid floating point number between (and including) 20.000,00 and 80.000,00.
#   - Date: only in YYYY-MM-DD format, no negative numbers, days between 1 - 31, month between 1 - 12, year only 2021 and 2022.
# - Feedback: if the email contains a feedback there is an extra line in the text otherwise that line must be removed.
# - The program will generate emails until the user answers No to the More Letters? question.
# - In case of invalid input from the user, the program must print the message Input error and then repeat the question again.
#
# https://app.codegra.de/courses/5199/assignments/38791/submissions#description

# Type
type_email = "Job Offer / Rejection Email"

# Global
first_name = "FIRST_NAME"
last_name = "LAST_NAME"
job_title = "JOB_TITLE"

# Job Offer
anual_salary = "ANUAL_SALARY"
starting_date = "YYYY-MM-DD"

# Rejection
with_feedback = "FEEDBACK_BOOLEAN"
feedback = "FEEDBACK_PLACEHOLDER"


def prepare_email(email_properties):
    if email_properties[0].lower() == "job offer" or email_properties[0].lower() == "jo":
        anual_salary = input("")
        email_properties.append(anual_salary)
        starting_date = input("")
        email_properties.append(starting_date)

    elif email_properties[0].lower() == "rejection" or email_properties[0].lower() == "rej":
        with_feedback = input("")
        email_properties.append(with_feedback)

        if with_feedback.lower() == "yes":
            feedback = input("")
            email_properties.append(feedback)

    return email_properties


def send_email(email_properties):
    # print(email_properties)
    mail = ""
    mail += f'Dear {email_properties[1]} {email_properties[2]},\nAfter careful evaluation of your application for the position of {email_properties[3]},\n'

    if email_properties[0].lower() == "job offer" or email_properties[0].lower() == "jo":
        mail += (f'we are glad to offer you the job. Your salary will be {email_properties[4]} euro annually. \n'
                 f'Your start date will be on {email_properties[5]}. Please do not hesitate to contact us with any questions.')

    elif email_properties[0].lower() == "rejection" or email_properties[0].lower() == "rej":
        mail += f'at this moment we have decided to proceed with another candidate.\n'
        if email_properties[4].lower() == "yes":
            mail += (f'Here we would like to provide you our feedback about the interview.\n'
                     f'{email_properties[5]}')
        mail += (
            f'We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.')

    mail += "\nSincerely,\nHR Department of XYZ"

    print("Here is the final letter to send:")
    return mail


def main():
    more_letters = input("")

    if more_letters or more_letters.lower() == "yes":
        email_type = input("")
        first_name = input("")
        if len(first_name) < 2 or len(first_name) > 10:
            print("Input error")
            exit(1)
        last_name = input("")
        job_title = input("")

        email_properties = prepare_email([email_type, first_name, last_name, job_title])

        email = send_email(email_properties)

        print(email)


main()
