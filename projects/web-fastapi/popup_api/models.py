from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
    func,
    insert,
    select,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from popup_api.settings import settings  # isort:skip

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    connect_args=settings.DATABASE_CONNECT_ARGS,
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# ==========
# Data Model
# ==========


class Task(Base):
    __tablename__ = "popup_task"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="序号")
    name = Column(String(50), nullable=False, comment="任务名称")
    priority = Column(Integer, nullable=False, default=0, comment="任务优先级")
    description = Column(String(200), nullable=True, comment="任务描述", default="")
    create_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="创建时间",
    )
    update_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        comment="更新时间",
    )
    is_done = Column(Integer, nullable=False, default=0, comment="是否完成")
    group_id = Column(Integer, ForeignKey("popup_group.id"), default=1, comment="分类序号")

    def __repr__(self):
        return f"<Task(id={self.id}, name={self.name}, is_done={self.is_done}, group_id={self.group_id})>"


class Group(Base):
    __tablename__ = "popup_group"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="分类序号")
    name = Column(
        String(50),
        nullable=False,
        default="收集箱",
        comment="分类名称",
        unique=True,
    )

    def __repr__(self):
        return f"<Group(id={self.id}, name={self.name})"


# ============
# Data handler
# ============


def init_db():
    Base.metadata.create_all(engine)

    group_check = engine.execute(select(Group).limit(5)).all()

    if not group_check:
        groups = [
            dict(name="收集箱"),
            dict(name="生活"),
            dict(name="工作"),
        ]
        stmt = insert(Group).values(groups)
        engine.execute(stmt)

    task_check = engine.execute(select(Task).limit(5)).all()
    if not task_check:
        tasks = [
            dict(name="吃饭", priority=3, group_id=2),
            dict(name="睡觉", priority=3, group_id=2),
            dict(name="打豆豆", priority=0, description="打豆豆是一件很有意思的事情"),
            dict(name="逛逛少数派", priority=1, description="https://sspai.com"),
            dict(name="记得下班打卡", priority=3),
        ]

        stmt = insert(Task).values(tasks)
        engine.execute(stmt)


def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
