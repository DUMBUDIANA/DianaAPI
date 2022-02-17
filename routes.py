



from flask_restful import Resource
from repository import Repository
from flask import request

repository = Repository()


class BookList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
        
    def get(self):
        return [book.__dict__ for book
         in self.repo.books_get_all()]
    
    def post(self, req=request): 
       data = req.get_json()
       return self.repo.book_add(data).__dict__


class Book(Resource):
    def __init__(self, repo=repository):
        self.repo = repo


class ReviewList(Resource):
    def __init__(self, repo=repository):
        self.repo = repo


class Review(Resource):
    def __init__(self, repo=repository):
        self.repo = repo
