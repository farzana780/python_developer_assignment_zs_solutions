# Python Developer Assignment - ZS Solutions

In this project, I demonstrated the following set of skills:
1. Designed a database to store information about Countries, States and Addresses.
2. Designed APIs for listing and filtering all Countries, States and Addresses using different conditions.
3. Tested all APIs using Pytest
4. Established oauth2 authentication and Created a login API so the registered users can access the APIs by logging in. 
5. Ensured quality and ran checks in CI/CD pipeline using CircleCI.
## Setup

1. Git Clone the project with: ```https://github.com/farzana780/python_developer_assignment_zs_solutions.git```.

2. Move to the base directory: ```cd python_developer_assignment_zs_solutions```

3. Create a new python environment with: ```python -m venv env```.

4. Activate environment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

5. Install required dependencies with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app locally with: ```python manage.py runserver```.

## Instructions on Test 
1. Run the command to test all the APIs: ```pytest``` or ```py.test```
2. Run the commands to test specific APIs:
    * Country List: ```pytest -k countrylist```
    * Country Filter by Name: ```pytest -k country_filter_By_Name ```
    * Country Filter by Code: ```pytest -k country_filter_By_Code```
    * State List: ```pytest -k statelist```
    * State Filter By Name: ```pytest -k state_filter```
    * Address List: ```pytest -k addresslist```
    * Address Filter by House no: ```pytest -k address_By_HouseNumber```
    * Address Filter by Road no: ```pytest -k address_By_RoadNumber```
    * Address Details: ```pytest -k address_Details```
    
3. Run the commands to test specific API's Endpoints:
    * Country List URL: ```pytest -k countrylist_url```
    * Country Filter URL: ```pytest -k country_url```
    * State List URL: ```pytest -k statelist_url```
    * State Filter URL: ```pytest -k state_url```
    * Address List URL: ```pytest -k addresslist_url```
    * Address Filter by Road no URL: ```pytest -k address_rn_url```
    * Address Filter by House no URL: ```pytest -k address_hn_url```
    * Address Details URL: ```pytest -k addressDetails_url```