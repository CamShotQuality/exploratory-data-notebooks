import os

def load_connection_string(db_name: str) -> str:
    """
    Create a connection string to a PostgreSQL database.

    Required environment variables:
    - SHOTQUALITY_DB_USER
    - SHOTQUALITY_DB_PASSWORD
    - SHOTQUALITY_DB_HOST

    Args:
        db_name: The name of the database.

    Returns:
        str: The connection string.

    """
    # set os.getenv("SHOTQUALITY_DB_HOST", "") prod instance (setting in .env file does not pick up update)
    os.environ["SHOTQUALITY_DB_HOST"] = "shotquality-prod-1.c7t8xvfkmus6.us-east-1.rds.amazonaws.com"
    return (
        "postgresql://"
        + os.getenv("SHOTQUALITY_DB_USER", "")
        + ":"
        + os.getenv("SHOTQUALITY_DB_PASSWORD", "")
        + "@"
        + os.getenv("SHOTQUALITY_DB_HOST", "")
        + "/"
        + db_name
    )