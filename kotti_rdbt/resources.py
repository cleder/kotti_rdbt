from kotti.resources import Content
from kotti.resources import File
from kotti.util import JsonType
from kotti_rdbt import _
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode


class RDBTable(File):
    id = Column('id', Integer, ForeignKey('files.id'), primary_key=True)
    #XXX + table metadata


    type_info = Content.type_info.copy(
        name=u'Table',
        title=_(u'Table'),
        add_view=u'add_table',
        addable_to=[u'Document'],
        )

class RDBTableColumn(Content):
    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    column_name = Column(Unicode(40))
    column_type = Column(Unicode(10))
    column_lenght = Column(Integer)



    type_info = Content.type_info.copy(
        name=u'Column',
        title=_(u'Column'),
        add_view=u'add_column',
        addable_to=[u'Table'],
        )

    def __init__(self, column_name=None, column_type=None, column_lenght=0,
                 in_navigation=False, **kwargs):
        super(RDBTableColumn, self).__init__(in_navigation=in_navigation, **kwargs)
        self.column_name = column_name
        self.column_type = column_type
        self.column_lenght = column_lenght