from flask import Flask, jsonify, request
from app import connection

app = Flask(__name__)

@app.route('/account/<int:id>', methods=['GET'])
def get_account(id):
    conn = connection()
    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public.accounts WHERE id = %s', (id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        account = {
            'id': result[0],
            'account_number': result[1],
            'account_type' : result[2],
            'balance': result[3],
        }
        return jsonify(account)
    else:
        return jsonify({'error': 'Account not found'}), 404

@app.route('/account/<int:id>', methods=['PUT,'])
def update_account(id):
    # Connect to the database
    conn = connection()

    # Retrieve data from request body
    data = request.get_json()
    id = data.get('id')
    new_balance = data.get('balance')
   
    # Execute the SQL query to update the admin
    cursor = conn.cursor()
    cursor.execute('UPDATE public.accounts SET balance = %s,  WHERE id = %s',(new_balance, id))

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return success response
    return jsonify({'message': 'Account updated successfully'})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_account(id):
    # Connect to the database
    conn = connection()

    # Execute the SQL query to delete the admin
    cursor = conn.cursor()
    cursor.execute('DELETE FROM public.accounts WHERE id = %s', (id,))

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return success response
    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)