import os
from sqlalchemy.orm import Session
from strategies.storageStrategy import StorageStrategy
from strategies.dbStorageStrategy import DBStorageStrategy
from strategies.listStorageStrategy import ListStorageStrategy
from db.session import AppConfig

def get_storage_strategy(use_db=True) -> StorageStrategy:  
    if use_db:
        database_url = "postgresql://avnadmin:AVNS_NGzNN3n0QEnjHmyp18m@indicai-pg-indicai.c.aivencloud.com:20466/defaultdb?sslmode=require" 
        app_config = AppConfig(database_url=database_url)
        db: Session = next(app_config.get_db_session())  
        return DBStorageStrategy(db)
    else:
        return ListStorageStrategy()

