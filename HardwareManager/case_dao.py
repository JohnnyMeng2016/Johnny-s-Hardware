from sqlalchemy import Column, String, Integer, Float, DateTime, and_
from data_access import Base, DBSession
import config


class Case(Base):
    __tablename__ = 'product_case'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    caseType = Column(String(30))
    structure = Column(String(30))
    smallPosition = Column(String(30))
    bigPosition = Column(String(30))
    panelPort = Column(String(50))
    powerSupport = Column(String(30))
    caseTheme = Column(String(30))
    caseMaterial = Column(String(50))
    extSlot = Column(String(30))
    weight = Column(String(30))
    mainboardSupport = Column(String(30))
    fan = Column(String(50))
    lineMode = Column(String(30))
    zolScore = Column(Float)
    image = Column(String(300))
    page = Column(Integer)

    def save_case(self, case):
        session = DBSession()
        session.add(case)
        session.commit()
        session.close()

    def save_cases(self, cases):
        session = DBSession()
        for case in cases:
            session.add(case)
        session.commit()
        session.close()

    def get_cases_by_condition(self, name, page):
        session = DBSession()
        c = []
        if name is not None:
            c += [Case.name.like("%name%")]
        __cases = session.query(Case).filter(and_(*c)).offset((int(page) - 1) * config.pageSize).limit(config.pageSize)
        session.close()
        return __cases

    def get_case_count(self, name):
        session = DBSession()
        where = ''
        if name is not None:
            where += ' and name=' + name
        count = session.execute('select count(1) as count from product_case where 1 = 1' + where).first().count
        session.close()
        return count


if __name__ == '__main__':
    # __cpu = Cpu(zolId='3232', name='I7', category='中文')
    # __cpu.save_cpu(__cpu)
    __case = Case()
    print(__case.get_case_count(None))
