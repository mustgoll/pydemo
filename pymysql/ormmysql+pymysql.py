import sqlalchemy
from  sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine=create_engine('mysql+pymysql://helin:abcd1234@localhost/helin?charset=utf8',encoding='utf-8',echo=False)

Base=declarative_base()
class User(Base):
    __tablename__='ormtest'
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    age=Column(Integer)

    def __repr__(self):
        return '(%s--%s)' %(self.name,self.age)

Base.metadata.create_all(engine)

session_class=sessionmaker(bind=engine)
Session=session_class()
# add1=User(name='ss',age=10)
# add2=User(name='wcj',age=23)
# Session.add_all([add1,add2])
data=Session.query(User).filter(User.id>0).all()
print(data)
Session.commit()