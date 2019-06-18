from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from app import app, models, db

manager = Manager(app)

# 将app和db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # 运行当前Flask应用程序
    manager.run()
