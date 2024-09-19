import os
from sqlalchemy.orm import Session
from api_indicai.strategies.storageStrategy import StorageStrategy
from api_indicai.strategies.dbStorageStrategy import DBStorageStrategy
from api_indicai.strategies.listStorageStrategy import ListStorageStrategy
from api_indicai.db.session import AppConfig

def get_storage_strategy() -> StorageStrategy:
    
    use_db = True  
    
    if use_db:
        database_url = "" 
        app_config = AppConfig(database_url=database_url)
        db: Session = next(app_config.get_db_session())  
        return DBStorageStrategy(db)
    else:
        return ListStorageStrategy()

