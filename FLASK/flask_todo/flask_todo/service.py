
from models import ToDoModel
from loguru import logger

# Service.py
class ToDoService:
    def __init__(self):
        self.model = ToDoModel()
        
    def create(self, params):
        logger.info(self.model.create(params["Title"], params["Description"]))
        logger.info(params["Title"])
        logger.info(params["Description"])
        return self.model.create(params["Title"], params["Description"])
