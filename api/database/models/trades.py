from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from ...database.base_class import Base

class Trade(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    exchange = Column(String, nullable=False)
    exchange_url = Column(String)
    token1 = Column(String, nullable=False)
    token2 = Column(String, nullable=False)
    description = Column(String)
    date_trade  = Column(Date)
    is_active = Column(Boolean(), default=True)
    trader_id = Column(Integer, ForeignKey('user.id'))
    trader = relationship('User', back_populates = 'trades')