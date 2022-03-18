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
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute(
            "select title, author, bookId, cover from book order by title")
            book_records = ps_cursor.fetch_one()
            book_list = []
            for row in book_records:
                    book_list.append(BookModel(row[0], row[1], row[2], row[3]))
            ps_cursor.close()
            return book_list

        
        

    def reviews_get_by_book_id(self, book_id):
       conn = self.get_db()
       if (conn):
           ps_cursor = conn.cursor()
           ps_cursor.execute(
           "select content,bookId from review order by content")
           review_records = ps_cursor.fetch_one()
           review_list = []
           for row in review_records:
                    review_list.append(ReviewModel(row[0], row[1]))
           ps_cursor.close()
           return review_list


    def review_add(self, data):
          conn = self.get_db()
          if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute(
                    "INSERT INTO review(content,bookId) VALUES (%s, %s) RETURNING bookId",
                    (data['content'], data['bookId']))
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close()
                review = ReviewModel(data['content'], id,
                                 data['author'], data['cover'])
          return review
        

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
         

