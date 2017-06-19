from sqlalchemy import Column, String, Integer, Float, DateTime, and_
from data_access import Base, DBSession
import config


class Graph(Base):
    __tablename__ = 'product_graph'

    id = Column(Integer, primary_key=True)
    zolId = Column(String(20))
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Integer)
    coreType = Column(String(30))
    port = Column(String(30))
    chipset = Column(String(30))
    ram = Column(String(30))
    bit = Column(String(30))
    coreFrequency = Column(String(30))
    vmFrequency = Column(String(30))
    fanType = Column(String(30))
    zolScore = Column(Float)
    image = Column(String(300))
    page = Column(Integer)

    def save_graph(self, graph):
        session = DBSession()
        session.add(graph)
        session.commit()
        session.close()

    def save_graphs(self, graphs):
        session = DBSession()
        for graph in graphs:
            session.add(graph)
        session.commit()
        session.close()

    def get_graphs_by_condition(self, name, page):
        session = DBSession()
        c = []
        if name is not None:
            c += [Graph.name.like("%name%")]
        __cpus = session.query(Graph).filter(and_(*c)).offset((int(page) - 1) * config.pageSize).limit(config.pageSize)
        session.close()
        return __cpus

    def get_graph_count(self, name):
        session = DBSession()
        where = ''
        if name is not None:
            where += ' and name=' + name
        count = session.execute('select count(1) as count from product_graph where 1 = 1' + where).first().count
        session.close()
        return count


if __name__ == '__main__':
    # __cpu = Cpu(zolId='3232', name='I7', category='中文')
    # __cpu.save_cpu(__cpu)
    __graph = Graph()
    print(__graph.get_graph_count(None))
