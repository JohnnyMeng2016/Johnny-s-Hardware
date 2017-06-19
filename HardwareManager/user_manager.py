from user_dao import User


class usermanger:
    def login(self, username, password):
        __userDao = User()
        __users = __userDao.get_user_by_condition(None, username, password)
        if __users.count() > 0:
            return True
        else:
            return False

    def get_user_list(self):
        __userDao = User()
        __users = __userDao.get_user_by_condition(None, None, None)
        return __users

    def get_user_by_condition(self, userId, username):
        __userDao = User()
        __users = __userDao.get_user_by_condition(userId, username, None)
        return __users.first()
