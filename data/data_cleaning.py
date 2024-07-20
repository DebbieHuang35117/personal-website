from unstructured.partition.html import partition_html
import os
from tqdm import tqdm


def clean_faculty_data(faculty_number: int) -> dict:
    filename = os.path.join(os.path.dirname(__file__),
                            f"../data/faculty/{faculty_number}.html")
    elements = partition_html(filename=filename)
    cleaned_data = []

    for element in elements:
        if element.category == "UncategorizedText":
            cleaned_data.append(cleaned_data)

    return "\n\n".join([str(el) for el in cleaned_data])


if __name__ == "__main__":
    faculty_limit = 1
    for faculty_number in tqdm(range(faculty_limit), desc="Cleaning HTML files"):
        cleaned_data = clean_faculty_data(faculty_number=faculty_number)
        with open(os.path.join(os.path.dirname(__file__), f"../data/faculty_cleaned/{faculty_number}.txt"), "w") as file:
            file.write(cleaned_data)
