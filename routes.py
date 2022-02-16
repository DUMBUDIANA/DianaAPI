from flask_restful import Resource
from repository import Repository
from flask import request

repo = Repository()


class BookList(Resource):
    def get(self):
        return [book.__dict__ for book in repo.books_get_all()]

    def post(self):
        data = request.get_json()
        return repo.book_add(data).__dict__


class Book(Resource):
    def get(self):
        return{'hello': 'from book{book_id}'}


class ReviewList(Resource):
    def get(self, book_id):
        return [review.__dict__ for review in repo.reviews_get_by_book_id(int(book_id))]


class Review(Resource):
    def post(self):
        data = request.get_json()
        return repo.review_add(data).__dict__
