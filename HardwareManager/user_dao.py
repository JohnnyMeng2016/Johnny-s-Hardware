from sqlalchemy import Column, String, Integer, DateTime, and_
from data_access import Base, DBSession


class User(Base):
    __tablename__ = 'user'

    userId = Column(Integer, primary_key=True)
    userName = Column(String(100))
    password = Column(String(100))
    createTime = Column(DateTime)
    lastLoginTime = Column(DateTime)
    role = Column(Integer)

    def get_user_by_condition(self, userId, username, password):
        session = DBSession()
        c = []
        if userId is not None:
            c += [User.userId == userId]
        if username is not None:
            c += [User.userName == username]
        if password is not None:
            c += [User.password == password]
        __users = session.query(User).filter(and_(*c))
        session.close()
        return __users


if __name__ == '__main__':
    userDao = User()
    users = userDao.get_user_by_condition(3, None, None)
    print(users.first())
