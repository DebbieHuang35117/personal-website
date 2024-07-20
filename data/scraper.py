import requests
import os

if __name__ == "__main__":
    # This is a script to scrape the information of different faculty members from the website of the National Taiwan University Information Management Department.

    url_template = "https://management.ntu.edu.tw/IM/faculty/teacher/sn/"
    faculty_number = 0
    faculty_limit = 100

    while faculty_number < faculty_limit:
        url = url_template + str(faculty_number)
        response = requests.get(url)
        with open (os.path.join(os.path.dirname(__file__), f"../data/faculty/{faculty_number}.html"), "w") as file:
            file.write(response.text)
        faculty_number += 1
