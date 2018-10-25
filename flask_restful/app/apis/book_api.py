from flask_restplus import fields, Namespace, Resource

from app.models import Book
from ._api import api

ns = Namespace('books', description='Books 增删改查 .')

book_model = ns.model('BookModel', {
    'book_id': fields.String(readOnly=True, description='The book unique identifier'),
    'book_name': fields.String(required=True, description='The book nickname'),
    'price': fields.String(required=True, description='The book price'),
})
book_list_model = ns.model('BookListModel', {
    'books': fields.List(fields.Nested(book_model)),
    'total': fields.Integer,
})


@ns.route("")
class BookListApi(Resource):
    # 初始化数据
    books = [Book("三体", '100'), Book("解忧杂货铺", '25')]

    @ns.doc('get_book_list')
    @ns.marshal_with(book_list_model)
    def get(self):
        return {
            "books": self.books,
            "total": len(self.books),
        }

    @ns.doc('create_book')
    @ns.expect(book_model)
    @ns.marshal_with(book_model, code=201)
    def post(self):
        print(api.payload['book_name'], '++++')
        book = Book(api.payload['book_name'], api.payload['price'])
        return book