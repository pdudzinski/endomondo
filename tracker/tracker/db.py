from zope.sqlalchemy import ZopeTransactionExtension

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class TrackerBase(object):
    
    def __init__(self, *args, **kwargs):
        self.fill_with_kwargs(*args, **kwargs)
    
    @classmethod
    def get(cls, object_id):
        return DBSession.query(cls).filter(cls.id == object_id).first()
        
    @classmethod
    def all(cls):
        return DBSession.query(cls).all()
        
    def fill_with_kwargs(self, *args, **kwargs):
        for k, v in kwargs.iteritems():
            if v not in (None, ''):
                setattr(self, k, v)
        return self
