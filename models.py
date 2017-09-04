from sqlalchemy import Column, Integer, String, Text
from database import Base

class AppDetails(Base):
    __tablename__ = 'app_details'
    id = Column (Integer, primary_key=True)
    package = Column (String(256), unique=True)
    desc = Column (Text)

    def __init__ (self, package, desc):
        self.package = package
        self.desc = desc

    def __repr__(self):
        return '<App %r>' % (self.package)