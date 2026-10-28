from datetime import datetime
from sqlalchemy import String, Integer, BigInteger, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Booking(Base):
    __tablename__ = "bookings"
