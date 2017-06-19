from sqlalchemy import Column, String, Integer, Float, DateTime, and_
from data_access import Base, DBSession
import config


class Cpu(Base):
    __tablename__ = 'product_cpu'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    socketType = Column(String(30))
    frequency = Column(String(30))
    turboFrequency = Column(String(30))
    craftsmanship = Column(String(20))
    secondCache = Column(String(20))
    thirdCache = Column(String(20))
    coreNum = Column(String(30))
    coreCode = Column(String(30))
    tdp = Column(String(10))
    ht = Column(String(20))
    zolScore = Column(Float)
    image = Column(String(300))
    page = Column(Integer)

    def save_cpu(self, cpu):
        session = DBSession()
        session.add(cpu)
        session.commit()
        session.close()

    def save_cpus(self, cpus):
        session = DBSession()
        for cpu in cpus:
            session.add(cpu)
        session.commit()
        session.close()

    def get_cpus_by_condition(self, name, page):
        session = DBSession()
        c = []
        if name is not None:
            c += [Cpu.name.like("%name%")]
        __cpus = session.query(Cpu).filter(and_(*c)).offset((int(page) - 1) * config.pageSize).limit(config.pageSize)
        session.close()
        return __cpus

    def get_cpu_count(self, name):
        session = DBSession()
        where = ''
        if name is not None:
            where += ' and name=' + name
        count = session.execute('select count(1) as count from product_cpu where 1 = 1' + where).first().count
        session.close()
        return count


if __name__ == '__main__':
    # __cpu = Cpu(zolId='3232', name='I7', category='中文')
    # __cpu.save_cpu(__cpu)
    __cpu = Cpu()
    print(__cpu.get_cpu_count(None))
