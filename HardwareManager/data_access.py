from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
engine = create_engine('mysql+pymysql://root:1231131@127.0.0.1:3306/hardware_maker?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)



