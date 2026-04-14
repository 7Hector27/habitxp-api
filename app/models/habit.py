from sqlalchemy import Column, String, Time, Date, DateTime, ARRAY, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.session import Base
import uuid
from datetime import datetime

class Habit(Base):
    __tablename__ = "habits"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    emoji = Column(String, nullable=True)
    color = Column(String, nullable=True)
    priority = Column(String, nullable=True)
    category = Column(String, nullable=True)
    type = Column(String, nullable=False, default="boolean")
    target_value = Column(String, nullable=True)
    target_unit = Column(String, nullable=True)
    frequency = Column(ARRAY(String), nullable=True)
    notification_type = Column(String, nullable=True)
    notification_time = Column(Time, nullable=True)
    start_date = Column(Date, nullable=True)
    archived_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="habits")