from models import BookModel, ReviewModel
import psycopg2
from flask import current_app, g






# HOST = os.environ.get("HOST")
# DATABASE = os.environ.get("DATABASE")
# DB_PORT = os.environ.get("DB_PORT")
# USER = os.environ.get("USER")
# PASSWORD = os.environ.get("PASSWORD")


class Repository():
    def get_db(self):
       if 'db' not in g:
           g.db = current_app.config['pSQL_pool'].getconn()
           return g.db

    def books_get_all(self):
            conn = self.get_db() 
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                "select title, author, bookId, cover from book order by title")
                book_records = ps_cursor.fetchall()
                book_list = []
                for row in book_records:
                    book_list.append(BookModel(row[0], row[1], row[2], row[3]))
                ps_cursor.close() 
                return book_list



    




               

    def book_get_by_id(self, book_id):
        books = [book1, book2]
        return next((x for x in books if x.bookId == book_id), None)
        

    def reviews_get_by_book_id(self, book_id):
       reviews = [review1,review2,review3,review4]
       return [x for x in reviews if x.bookId == book_id]

    def review_add(self, data):
       return ReviewModel(data['content'], data['bookId'], 1)

    def book_add(self, data):
             conn = self.get_db() 
             if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    "INSERT INTO book(title,cover,author) VALUES (%s, %s, %s) RETURNING bookId",
                    (data['title'], data['cover'], data['author']))
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close() 
                book = BookModel(data['title'], id,
                                 data['author'], data['cover'])
             return book
         

