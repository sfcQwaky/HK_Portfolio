from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, DateTime
from datetime import datetime

app = Flask(__name__)


class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my_protfolio.db"
db = SQLAlchemy(model_class=Base)

db.init_app(app)

'''
    - project title
    - project short description
    - project detail description
    - project future vision and updates
    - github link
'''

class Record(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    short_desc: Mapped[str] = mapped_column(String(80), nullable=False)
    detail_desc: Mapped[str] = mapped_column(Text, nullable=False)
    future_vision: Mapped[str] = mapped_column(String(250), nullable=False)
    github_link: Mapped[str] = mapped_column(String(250), nullable=False)
    latest_update: Mapped[str] = mapped_column(DateTime, nullable=False)

with app.app_context():
    db.create_all()

# with app.app_context():
#     new_record = Record(title="Title of project 4",
#                         short_desc="Video provides a powerful way to help you prove your point.",
#                         detail_desc="When you click Online Video, you can paste in the embed code for the video you"
#                                     " want to add. You can also type a keyword to search online for the video that best fits your document. .\n"
#                                     "Click Insert, then choose the elements you want from the different galleries. Themes and styles also help to keep your document coordinated."
#                                     "\n\n"
#                                     "To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add "
#                                     "a row or a column, then click the plus sign. Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. "
#                                     "If you need to stop reading before you reach the end, Word remembers where you finished – even on another device."
#                                     "\n"
#                                     "Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. "
#                                     "You can also type a keyword to search online for the video that best fits your document.",
#                         future_vision="To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, "
#                                       "click where you want to add a row or a column, then click the plus sign.",
#                         github_link="https://github.com/sfcQwaky/temp4",
#                         latest_update=datetime.now().replace(microsecond=0)
#                       )
#     db.session.add(new_record)
#     db.session.commit()
#     print("New record created")