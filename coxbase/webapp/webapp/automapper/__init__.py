from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.ext.automap import automap_base 


class Automapper():
    def __init__(self, config_path):
        self.config_path = config_path
        self.settings = get_appsettings(self.config_path,
                                        name="main")


    def generate_base(self, db):
        engine = engine_from_config(self.settings, db)
        Base = automap_base()
        Base.prepare(engine, reflect=True)
        return Base.classes

    def get_mapped_class(Base, table_name):
        return getattr(Base, table_name)


