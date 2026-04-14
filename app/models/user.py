from sqlalchemy import Column, String, Time, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship
 

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    oauth_provider = Column(String, nullable=False)
    oauth_id = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    avatar_url = Column(String, nullable=True)
    timezone = Column(String, nullable=True)
    end_of_day_reminder_time = Column(Time, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    habits = relationship("Habit", back_populates="user")
    achievements = relationship("UserAchievement", back_populates="user")