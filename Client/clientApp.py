import requests
import json


def CountPersonnelWithSalaryMoreThan(fromSalary):
    """Count personnel with salary more than asked

    Args:
        fromSalary (int): salary

    Returns:
        int: count of workers with an salary more than asked"""
    response = requests.get(
        'http://127.0.0.1:5000/personnelmanaging/api/v1.0/get_all_personnel')
    personnel_json = (json.loads(response.text))

    desiredSalaryPersonnel = [
        p for p in personnel_json['all_personnel'] if p['salary'] > fromSalary]
    return len(desiredSalaryPersonnel)


def main():
    print(CountPersonnelWithSalaryMoreThan(10000))


if __name__ == "__main__":
    main()
