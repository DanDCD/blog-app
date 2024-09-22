from google.cloud import firestore


def get_env_vars():
    import os
    from dotenv import load_dotenv

    load_dotenv() # sets all the variables in the .env file as environment variables
    # retrieve the environment variables and return them as a dictionary
    return {
        "app_credentials": os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
        "project_id": os.getenv("PROJECT_ID"),
    }


if __name__ == "__main__":
    env_vars = get_env_vars()

    db = firestore.Client(project=env_vars["project_id"])
    # check if the client is authenticated
    
