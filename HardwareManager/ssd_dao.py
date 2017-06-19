from sqlalchemy import Column, String, Integer, Float, DateTime, and_
from data_access import Base, DBSession
import config


class SSD(Base):
    __tablename__ = 'product_ssd'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    size = Column(String(30))
    port = Column(String(30))
    readSpeed = Column(String(30))
    writeSpeed = Column(String(30))
    inchType = Column(String(30))
    warranty = Column(String(30))
    architecture = Column(String(30))
    chipset = Column(String(30))
    seekTime = Column(String(30))
    fourKRandom = Column(String(30))
    zolScore = Column(Float)
    image = Column(String(300))
    page = Column(Integer)

    def save_ssd(self, ssd):
        session = DBSession()
        session.add(ssd)
        session.commit()
        session.close()

    def save_ssds(self, ssds):
        session = DBSession()
        for ssd in ssds:
            session.add(ssd)
        session.commit()
        session.close()

    def get_ssds_by_condition(self, name, page):
        session = DBSession()
        c = []
        if name is not None:
            c += [SSD.name.like("%name%")]
        __hdds = session.query(SSD).filter(and_(*c)).offset((int(page) - 1) * config.pageSize).limit(config.pageSize)
        session.close()
        return __hdds

    def get_ssd_count(self, name):
        session = DBSession()
        where = ''
        if name is not None:
            where += ' and name=' + name
        count = session.execute('select count(1) as count from product_ssd where 1 = 1' + where).first().count
        session.close()
        return count


if __name__ == '__main__':
    # __cpu = Cpu(zolId='3232', name='I7', category='中文')
    # __cpu.save_cpu(__cpu)
    __ssd = SSD()
    print(__ssd.get_ssd_count(None))
