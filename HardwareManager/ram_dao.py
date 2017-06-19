from sqlalchemy import Column, String, Integer, Float, DateTime, and_
from data_access import Base, DBSession
import config


class Ram(Base):
    __tablename__ = 'product_ram'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    size = Column(String(30))
    desc = Column(String(50))
    ddrType = Column(String(20))
    frequency = Column(String(20))
    cl = Column(String(50))
    pin = Column(String(30))
    voltage = Column(String(30))
    zolScore = Column(Float)
    image = Column(String(300))
    page = Column(Integer)

    def save_ram(self, ram):
        session = DBSession()
        session.add(ram)
        session.commit()
        session.close()

    def save_rams(self, rams):
        session = DBSession()
        for ram in rams:
            session.add(ram)
        session.commit()
        session.close()

    def get_rams_by_condition(self, name, page):
        session = DBSession()
        c = []
        if name is not None:
            c += [Ram.name.like("%name%")]
        __rams = session.query(Ram).filter(and_(*c)).offset((int(page) - 1) * config.pageSize).limit(config.pageSize)
        session.close()
        return __rams

    def get_ram_count(self, name):
        session = DBSession()
        where = ''
        if name is not None:
            where += ' and name=' + name
        count = session.execute('select count(1) as count from product_ram where 1 = 1' + where).first().count
        session.close()
        return count


if __name__ == '__main__':
    __ram = Ram()
    print(__ram.get_ram_count(None))
