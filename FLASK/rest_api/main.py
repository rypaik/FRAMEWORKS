from dotenv import load_dotenv
from dotenv import dotenv_values
import os 
# loading environment variables
load_dotenv()



#loading as dictionary
config = dotenv_values(".env")
print(config)

# to get variable

mysql_host=os.environ.get('MYSQL_HOST')
 
print(mysql_host)