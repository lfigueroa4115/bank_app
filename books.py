"""from flask import Flask, jsonify, request
from app import connection, db
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app, db)

@app.route('/books', methods=['GET'])
def get_books():
    # Connect to the database
    conn = connection()

    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public.books')
    results = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Convert the results to a list of dictionaries
    books = []
    for result in results:
        book = {
            'id': result[0],
            'title': result[1],
            'status' : result[2],
            'admin_id': result[3],
            'publisher' : result[4],
            'author': result[5]
            
        }
        books.append(book)

    # Return the JSON response
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def show_books(id):
    conn = connection()
    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public.books WHERE id = %s', (id,))
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    conn.close()

    if result:
        book = {
            'id': result[0],
            'title': result[1],
            'status' : result[2],
            'admin_id': result[3],
            'publisher' : result[4],
            'author': result[5],
        }
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def create_books():

    conn = connection()
    # Retrieve data from request body
    data = request.get_json()
    title = data.get('title')
    status = data.get('status')
    admin_id = data.get('admin_id')
    publisher = data.get('publisher')
    author= data.get('author')

    # Execute the SQL query to insert new admin
    cursor = conn.cursor()
    cursor.execute('INSERT INTO public.books (title,status,admin_id,publisher,author) VALUES (%s, %s, %s, %s, %s )', (title, status,admin_id,publisher,author))

    # Close the database connection
    cursor.close()
    conn.close()

    # Return success response
    return jsonify({'message': 'Book created successfully'})

@app.route('/books/<int:id>', methods=['PUT,'])
def update_book(id):
    # Connect to the database
    conn = connection()

    # Retrieve data from request body
    data = request.get_json()
    id = data.get('id')
    new_title = data.get('title')
    new_status = data.get('status')
    new_admin_id = data.get('admin_id')
    new_publisher = data.get('publisher')
    new_author= data.get('author')

    # Execute the SQL query to update the admin
    cursor = conn.cursor()
    cursor.execute('UPDATE public.books SET title = %s, status = %s, admin_id = %s, publisher = %s, author = %s WHERE id = %s',(new_title, new_status, new_admin_id,new_publisher, new_author, id))

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return success response
    return jsonify({'message': 'Book updated successfully'})


@app.route('/books/<int:id>', methods=['PATCH'])
def update_book_2(id):

    conn = connection()

    data = request.get_json()
    new_title = data.get('title')
    new_status = data.get('status')
    new_admin_id = data.get('admin_id')
    new_publisher = data.get('publisher')
    new_author = data.get('author')

    cursor = conn.cursor()
    query = 'UPDATE public.books SET '
    query_update = []
    if new_title is not None:
        query += 'title = %s, '
        query_update.append(new_title)
    if new_status is not None:
        query += 'status = %s, '
        query_update.append(new_status)
    if new_admin_id is not None:
        query += 'admin_id = %s, '
        query_update.append(new_admin_id)
    if new_publisher is not None:
        query += 'publisher = %s, '
        query_update.append(new_publisher)
    if new_author is not None:
        query += 'author = %s, '
        query_update.append(new_author)

    query = query.rstrip(', ')

    query += ' WHERE id = %s'
    query_update.append(id)

    cursor.execute(query, tuple(query_update))

    cursor.close()
    conn.close()

    return jsonify({'message': 'Book record updated successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)




@app.route('/books/<int:id>', methods=['DELETE'])
def delete_admin(id):
    # Connect to the database
    conn = connection()

    # Execute the SQL query to delete the admin
    cursor = conn.cursor()
    cursor.execute('DELETE FROM public.books WHERE id = %s', (id,))

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return success response
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)"""