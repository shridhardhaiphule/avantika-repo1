import os
from dotenv import load_dotenv

class EnvConstants:
    ENV_CONSTANTS = {}

    @staticmethod
    def load_env():
        app_env = os.getenv("APP_ENV", "dev")

        app_root = os.path.dirname(__file__)
        env_file_name = f".env.{app_env}"
        dotenv_path = os.path.join(app_root, env_file_name)

        load_dotenv(dotenv_path)

        EnvConstants.ENV_CONSTANTS = {
            "MONGO_CONNECTION_URL": os.getenv("MONGO_CONNECTION_URL"),
            "MONGO_DB_NAME": os.getenv("MONGO_DB_NAME"),
            "MONGO_COLLECTION_EMPLOYEES": os.getenv("MONGO_COLLECTION_EMPLOYEES")
        }

        return EnvConstants.ENV_CONSTANTS
