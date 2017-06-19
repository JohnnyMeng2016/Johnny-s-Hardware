from sqlalchemy import Column, String, Integer, Float, DateTime, and_, or_
from data_access import Base, DBSession
import config


class Power(Base):
    __tablename__ = 'product_power'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    ratedPower = Column(String(30))
    maxPower = Column(String(30))
    powerVersion = Column(String(30))
    support = Column(String(50))
    fan = Column(String(50))
    powerType = Column(String(50))
    other = Column(String(50))
    plusAuth = Column(String(50))
    safeAuth = Column(String(50))
    pfc = Column(String(50))
    safeFunction = Column(String(50))
    voltageSupport = Column(String(50))
    lineMode = Column(String(50))
    zolScore = Column(Float)
    image = Column(String(300))
    page = Column(Integer)

    def save_power(self, power):
        session = DBSession()
        session.add(power)
        session.commit()
        session.close()

    def save_powers(self, powers):
        session = DBSession()
        for power in powers:
            session.add(power)
        session.commit()
        session.close()

    def delete_all_powers(self):
        session = DBSession()
        session.execute('delete from product_power')
        session.commit()
        session.close()

    def get_powers_by_condition(self, condition, page):
        session = DBSession()
        where = ''
        if condition is not None:
            where += ' and name like "%' + condition + '%"'
        sql = 'select * from product_power where 1 = 1' + where + ' limit '+ str((int(page) - 1) * config.pageSize) + ',' + str(config.pageSize)
        __powers = session.execute(sql)
        session.close()
        return __powers

    def get_power_count(self, condition):
        session = DBSession()
        where = ''
        if condition is not None:
            where += ' and name like "%' + condition + '%"'
        count = session.execute('select count(1) as count from product_power where 1 = 1' + where).first().count
        session.close()
        return count


if __name__ == '__main__':
    __power = Power()
    __power.delete_all_powers()
