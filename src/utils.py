from github import Github, Auth
import pandas as pd
import numpy as np

def get_repo_from_github(token):
    """
    Gets the repository 'DIQ_Project2024' from GitHub.

    Parameters:
    - token: authentication key for GitHub.
    """
    # Authenticate using a personal access token
    auth_token = Auth.Token(token)
    github_client = Github(auth=auth_token)

    # Define the repository name you want to find
    target_repo_name = 'DIQ_Project2024'
    repo = None

    # Search for the repository in the user's repositories
    try:
        for repository in github_client.get_user().get_repos():
            if repository.name == target_repo_name:
                repo = repository
                print(f"Repository '{target_repo_name}' found.")
                break
        if repo is None:
            print(f"Repository '{target_repo_name}' not found.")
    except Exception as e:
        print("An error occurred while accessing the repositories:", e)

    return repo


def upload_file(filepath_kaggle, filepath_github, commit_message, repo=None):
    """
    Uploads a file from Kaggle to GitHub, updating it if it already exists in the repository,
    or creating it if it does not.

    Parameters:
    - filepath_kaggle: Path to the file in the Kaggle environment.
    - filepath_github: Target path in the GitHub repository where the file should be uploaded.
    - commit_message: Message for the commit on GitHub.
    """
    if repo is None:
        raise ValueError("Repository is not defined. Make sure to call 'get_repo_from_github' to get the repo instance before using this function.")
    
    try:
        
        # Check if the file already exists in the GitHub repository
        contents = repo.get_contents(filepath_github)
        
        # If it exists, update the file
        with open(filepath_kaggle, "rb") as file:
            repo.update_file(
                contents.path, commit_message, file.read(), contents.sha
            )
        print(f"File '{filepath_github}' updated successfully.")
    
    except Exception as e:
        
        # If the file does not exist, create it
        with open(filepath_kaggle, "rb") as file:
            repo.create_file(
                filepath_github, commit_message, file.read()
            )
        print(f"File '{filepath_github}' created successfully.")
