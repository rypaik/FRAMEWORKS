from dotenv import load_dotenv
from dotenv import dotenv_values

# loading environment variables
load_dotenv()



#loading as dictionary
config = dotenv_values(".env")
print(config)

# to get variable


# undefined 
print(f"{MYSQL_HOST}")