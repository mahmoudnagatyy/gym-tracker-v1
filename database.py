from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./gym.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class SessionDB(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    time = Column(String)
    session_type = Column(String)
    bodyweight = Column(Float, nullable=True)
    total_volume = Column(Float, default=0.0)
    total_sets = Column(Integer, default=0)
    duration = Column(Integer, default=0) # in seconds or minutes

    sets = relationship("SetDB", back_populates="session", cascade="all, delete-orphan")

class SetDB(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    exercise_name = Column(String, index=True)
    set_num = Column(Integer)
    weight_kg = Column(Float)
    reps = Column(Integer)
    volume = Column(Float)

    session = relationship("SessionDB", back_populates="sets")

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
