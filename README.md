
![Alt text](docs/git_setup.png)

This Python script allows you to manage environment variables in a GitLab project. You can use this script to add/update variables or delete existing ones in your GitLab project.
Prerequisites

## Before using this script, make sure you have the following:

- A GitLab Personal Access Token (PAT) - You can obtain a PAT from your GitLab account.

- Python environment - Ensure you have Python installed on your system.

- Python packages - Install the required Python packages using pip:

        pip install requests urllib3 python-dotenv

- A .env file - Create a .env file in the same directory as the script and define the following environment variables:

        TOKEN=your_gitlab_personal_access_token
        API_URL=https://your-gitlab-instance.com/api/v4
        G_SERVER=your_g_server_value
        P_DISKSTATION=your_p_diskstation_value
        P_TOKEN=your_p_token_value
        SONAR_HOST_URL=https://your-sonarqube-url.com/
        SONAR_TOKEN=your_sonarqube_token

## Usage

- Run the script by executing it with Python.

        python Gitlab_var_setup.py

- You will be prompted to choose between adding/updating (A) or deleting (D) variables.

### Adding/Updating Variables (A)

If you choose to add/update variables:

- The script will display the variables it's processing.
- It will check if each variable already exists in the project. If it does, it will update it. If not, it will add it.
- It will provide status messages for each operation, including success and error messages.

### Deleting Variables (D)

If you choose to delete variables:

- The script will retrieve the list of existing variables in the project.
- It will loop through the existing variables and delete each one.
- It will provide status messages for each deletion operation, including success and error messages.

# Disclaimer

Please note that this script requires proper GitLab permissions to perform these actions in your project.

Feel free to customize the script according to your specific project requirements.
Disclaimer

Use this script responsibly, and ensure that you have the necessary permissions to perform these actions in your GitLab project.

#