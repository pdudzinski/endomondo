# -*- coding: utf-8 -*-
import transaction

from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    and_,
    )

from ..db import (
    Base,
    DBSession,
    TrackerBase,
    )
    

class Workout(Base, TrackerBase):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    endomondo_id = Column(Integer, unique=True)
    name = Column(String(2000))
    distance = Column(Float(precision=2, asdecimal=True))
    start_time = Column(DateTime)
    duration = Column(DateTime)
    avg_speed = Column(Float(precision=2, asdecimal=True))
    
    def __init__(self, **kwargs):
        self.fill_with_kwargs(**kwargs)
        DBSession.add(self)
        transaction.commit()
        
    @classmethod
    def remove_all(cls):
        sql = "DELETE from workouts"
        DBSession.execute(sql)
        DBSession.flush()
        
    @property
    def pace(self):
        return 60/self.avg_speed

"""
CREATE TABLE workouts (
    id bigserial primary key,
    endomondo_id int not null, 
    name varchar(2000) not null,
    distance decimal(20,2) not null,
    start_time timestamp not null,
    duration decimal(20,2) not null,
    avg_speed decimal(20,2) not null
);
"""
