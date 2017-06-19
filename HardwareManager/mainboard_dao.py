from sqlalchemy import Column, String, Integer, Float, DateTime, and_
from data_access import Base, DBSession
import config

class MainBoard(Base):
    __tablename__ = 'product_mainboard'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    image = Column(String(300))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    socketType = Column(String(30))
    chipset = Column(String(30))
    ddrSupport = Column(String(30))
    cpuSupport = Column(String(50))
    integratedChip = Column(String(50))
    integratedGraph = Column(String(50))
    boardSize = Column(String(30))
    usbPort = Column(String(50))
    zolScore = Column(Float)
    page = Column(Integer)

    def save_mainboard(self, mainboard):
        session = DBSession()
        session.add(mainboard)
        session.commit()
        session.close()

    def save_mainboards(self, mainboards):
        session = DBSession()
        for mainboard in mainboards:
            session.add(mainboard)
        session.commit()
        session.close()

    def get_mainboards_by_condition(self, name, page):
        session = DBSession()
        c = []
        if name is not None:
            c += [MainBoard.name.like("%name%")]
        __mainboards = session.query(MainBoard).filter(and_(*c)).offset((int(page) - 1) * config.pageSize).limit(
            config.pageSize)
        session.close()
        return __mainboards

    def get_mainboards_count(self, name):
        session = DBSession()
        where = ''
        if name is not None:
            where += ' and name=' + name
        count = session.execute('select count(1) as count from product_mainboard where 1 = 1' + where).first().count
        session.close()
        return count

if __name__ == '__main__':
     __mainBoardDao = MainBoard(zolId='3232',name='I7',category='中文')
     __mainBoardDao.save_mainboard(__mainBoardDao)