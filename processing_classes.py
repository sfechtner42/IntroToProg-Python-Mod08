# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-processing_classes
# # Description: A collection of classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# Sabrina Fechtner, 12.3.2023, modified to only show read/write to file
# ------------------------------------------------------------------------------------------------- #
import json
from typing import TextIO, List
from data_classes import Employee

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Sabrina Fechtner 12.1.2023 Incorporated Class into A08
    """

    @staticmethod
    def read_data_from_file(file_name: str) -> List[Employee]:
        """ This function reads previous JSON file with employee data
        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated Function
        :param file_name: string data with the name of the file to read from
        :return: employee data as a list
        """
        file: TextIO = None
        employee_data = []
        employees: List[Employee] = []
        try:
            with open(file_name, "r") as file:
                employee_data = json.load(file)
                print("Data successfully loaded from the file.")
        except FileNotFoundError:
            print("File not found, creating it...")
            employee_data = [
                {"employee_first_name": "DefaultFirstName",
                 "employee_last_name": "DefaultLastName",
                 "review_date": "1900-01-01",
                 "review_rating": 3}
            ]
            with open(file_name, "w") as file:
                json.dump(employee_data, file)
                print("File created successfully.")
        except json.JSONDecodeError as e:
            print(f"Invalid JSON file: {e}. Resetting it...")
            # Resetting employee_data with default employee
            with open(file_name, "w") as file:
                json.dump(employee_data, file)
                print("File reset successfully.")
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")

        for row in employee_data:
            employee = Employee(row["employee_first_name"], row["employee_last_name"], row["review_date"],
                                row["review_rating"])
            employees.append(employee)
        return employees

    @staticmethod
    def write_data_to_file(file_name: str, employee_data: List[Employee]) -> List[Employee]:
        """ This function writes employee and review data to JSON file
        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function
        Sabrina Fechtner, 11.16.2023, Incorporated Function
        Sabrina Fechtner, 11.24.2023, Pulled into A07
        :param: file name = JSON file and roster = student data
        :return: None
        """
        file: TextIO = None
        from presentation_classes import IO
        try:
            json_data: List[dict[str, str, str, str, int]] = []
            for employee in employee_data:
                json_data.append({
                    "employee_first_name": employee.first_name,
                    "employee_last_name": employee.last_name,
                    "review_date": employee.review_date,
                    "review_rating": employee.review_rating
                })
            with open(file_name, "w") as file:
                json.dump(json_data, file)
                print("Data successfully written to the file.")
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return employee_data


if __name__ == "__main__":
    print("This class is not meant to be run!")
