import requests
import urllib3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Disable SSL warnings (use with caution)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the GitLab API headers with the Personal Access Token (PAT)
headers = {
    'PRIVATE-TOKEN': os.getenv('TOKEN'),
}

# GitLab API URL
api_url = os.getenv('API_URL')

# Specify the GitLab project ID where variables will be added
project_id = ""

# Define a dictionary of environment variables to be added to the project
variables_dico = {
    "DESIGN_N": "1",
    "MAJOR_N": "0",
    "MINOR_N": "0",
    "FEAT_M_R": "0",
    "FEAT_R": "0",
    "FIX_R": "0",
    "G_SERVER": os.getenv('G_SERVER'),
    "P_DISKSTATION": os.getenv('P_DISKSTATION'),
    "P_TOKEN": os.getenv('P_TOKEN'),
    "SONAR_HOST_URL": os.getenv('SONAR_HOST_URL'),
    "SONAR_TOKEN": os.getenv('SONAR_TOKEN')
}

# Prompt the user to choose between adding/updating or deleting variables
action = input("Do you want to add/update (A) or delete (D) variables? ").lower()

if action == 'a':
    for values in variables_dico:
        print(values + " : " + variables_dico[values])

        # Define parameters to be sent with the API request
        params = {'key': values, 'value': variables_dico[values]}

        # Make a GET request to check if the variable already exists in the project
        existing_var_response = requests.get(
            f'{api_url}/projects/{project_id}/variables/{values}',
            headers=headers,
            verify=False
        )

        if existing_var_response.status_code == 200:
            # If the variable exists, update it
            update_response = requests.put(
                f'{api_url}/projects/{project_id}/variables/{values}',
                headers=headers,
                verify=False,
                params=params
            )

            if update_response.status_code == 200:
                print(f"Updated variable: {values}")
            else:
                print(f"Error: Failed to update variable {values}. Status code: {update_response.status_code}")
        else:
            # If the variable doesn't exist, add it
            response = requests.post(
                f'{api_url}/projects/{project_id}/variables',
                headers=headers,
                verify=False,
                params=params
            )

            if response.status_code == 201:
                print(f"Added variable: {values}")
            else:
                print(f"Error adding variable {values}: {response.text}. Status code: {response.status_code}")

else:
    # Make a GET request to retrieve the list of existing variables in the project
    existing_vars_response = requests.get(
        f'{api_url}/projects/{project_id}/variables',
        headers=headers,
        verify=False
    )

    if existing_vars_response.status_code == 200:
        existing_variables = existing_vars_response.json()

        # Loop through existing variables and delete each one
        for existing_var in existing_variables:
            var_name = existing_var['key']
            delete_response = requests.delete(
                f'{api_url}/projects/{project_id}/variables/{var_name}',
                headers=headers,
                verify=False
            )

            if delete_response.status_code == 204:
                print(f"Deleted variable: {var_name}")
            else:
                print(f"Error: Failed to delete variable {var_name}. Status code: {delete_response.status_code}")
    else:
        print(f"Error: Failed to retrieve existing variables. Status code: {existing_vars_response.status_code}")
