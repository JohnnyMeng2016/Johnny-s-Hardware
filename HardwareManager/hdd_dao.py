from sqlalchemy import Column, String, Integer, Float, DateTime, and_
from data_access import Base, DBSession
import config


class Hdd(Base):
    __tablename__ = 'product_hdd'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    size = Column(String(30))
    port = Column(String(30))
    rpm = Column(String(30))
    cache = Column(String(30))
    portBit = Column(String(30))
    inchType = Column(String(30))
    zolScore = Column(Float)
    image = Column(String(300))
    page = Column(Integer)

    def save_hdd(self, hdd):
        session = DBSession()
        session.add(hdd)
        session.commit()
        session.close()

    def save_hdds(self, hdds):
        session = DBSession()
        for hdd in hdds:
            session.add(hdd)
        session.commit()
        session.close()

    def get_hdds_by_condition(self, name, page):
        session = DBSession()
        c = []
        if name is not None:
            c += [Hdd.name.like("%name%")]
        __cpus = session.query(Hdd).filter(and_(*c)).offset((int(page) - 1) * config.pageSize).limit(config.pageSize)
        session.close()
        return __cpus

    def get_hdd_count(self, name):
        session = DBSession()
        where = ''
        if name is not None:
            where += ' and name=' + name
        count = session.execute('select count(1) as count from product_hdd where 1 = 1' + where).first().count
        session.close()
        return count


if __name__ == '__main__':
    # __cpu = Cpu(zolId='3232', name='I7', category='中文')
    # __cpu.save_cpu(__cpu)
    __hdd = Hdd()
    print(__hdd.get_hdd_count(None))
