from sqlalchemy import create_engine
import unittest
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid import testing
from .models import DBFactory
from pyramid.request import Request
from pyramid.decorator import reify
from .requests import MyRequest

def create_db1_session(db_url):
    engine = create_engine(db_url)
    DBSession = sessionmaker(autoflush=False)
    DBSession.configure(bind=self.engine)
    metadata = Base.metadata
    metadata.bind = self.engine
    session = DBSession()
    return session

class MyRequet(Request):
    "override the pyramid request object to add explicit db session handling"

    @reify
    def db1_session(self):
        self.session = create_db1_session('mysql+pymysql://burnetii:crazyburnetii@localhost/cox')
        return self.session

       # self.add_finished_callback( self.close_dbs_1 )
       # return self.config.registry.db1_factory.get_sessin()

    @reify
    def db2_session(self, config):
        self.add_finished_callback( self.close_dbs_2 )
        return config.registry.db2_factory.get_session()

    def close_dbs_1(self, request):
        request.db1_session.close()

    def close_dbs_2(self, request):
        request.db2_session.close()

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(settings={'db1.url':
                                              'mysql+pymysql://burnetii:crazyburnetii@localhost/cox',
                                              'db2.url': 'mysql+pymysql://burnetii:crazyburnetii@localhost/cox'}) 
       # self.config.registry.db1_factory = DBFactory( db_url='mysql+pymysql://burnetii:crazyburnetii@localhost/cox')
       # self.config.registry.db2_factory = DBFactory( db_url= 'mysql+pymysql://burnetii:crazyburnetii@localhost/cox')
        self.config.include('.models') 
    def tearDown(self):
        testing.tearDown()


class TestMyViewSuccessCondition(BaseTest):
        from .models import organism, Features
        def test_default_view(self):
            config = self.config
            request = testing.DummyRequest(db1_session=MyRequet.db1_session)
            #  request.db1_session = req.db1_session()

            from .views.default import my_view
            response = my_view(request)
            self.assertEqual(response.status_code, 200)
  
#    def test_passing_view(self):
#        from .views.default import my_view
#        info = my_view(request)
#        self.assertEqual(info['Genus'], 'Coxiella')
#        self.assertEqual(info['project'], 'coxbase_webapp')


#class TestMyViewFailureCondition(BaseTest):
#
#    def test_failing_view(self):
#        from .views.default import my_view
#        info = my_view(dummy_request(self.session))
#        self.assertEqual(info.status_code, 200)
