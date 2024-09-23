from app import app, db
from flask import request, jsonify
from models import Friend

# CRUD (Create, Read, Update, Delete) Operations - Done!

# To get all friends
@app.route('/friends', methods=['GET'])
def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result)

# Creating a new friend
@app.route('/friends', methods=['POST'])
def create_friend():
    try :
        data = request.get_json()

        # Validating fa friend
        required_fields = ['name', 'age', 'role', 'gender', 'description']
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify({'error': f'Missing {field} field'}), 400

        name = data.get('name')
        age = data.get('age')
        role = data.get('role')
        gender = data.get('gender')
        description = data.get('description')


        # Fetching avatar image based on gender
        if gender == 'male':
            img_url = f'https://avatar.iran.liara.run/public/boy?username={name}'
        elif gender == 'female':
            img_url = f'https://avatar.iran.liara.run/public/girl?username={name}'
        else:
            img_url = None

        new_friend = Friend(name=name, age=age, role=role, description=description, gender=gender, img_url=img_url)

        db.session.add(new_friend)
        db.session.commit()

        return jsonify({'message': 'Friend created successfully!'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/friends/<int:id>', methods=['DELETE'])
def delete_friend(id):
    try:
        # Fetching the friend by ID
        friend = Friend.query.get(id)

        if friend is None:
            return jsonify({'error': 'Friend not found!'}), 404

        # Deleting the friend
        db.session.delete(friend)
        db.session.commit()
        return jsonify({'message': 'Friend deleted successfully!'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Updating a friend
@app.route('/friends/<int:id>', methods=['PATCH'])
def update_friend(id):
    try:
        friend = Friend.query.get(id)

        if friend is None:
            return jsonify({'error': 'Friend not found!'}), 404

        data=request.json
        friend.name=data.get('name',friend.name)
        friend.age=data.get('age',friend.age)
        friend.role=data.get('role',friend.role)
        friend.gender=data.get('gender',friend.gender)
        friend.description=data.get('description',friend.description)

        # Updating img_url after updating the name
        if friend.gender == 'male':
            friend.img_url = f'https://avatar.iran.liara.run/public/boy?username={friend.name}'
        elif friend.gender == 'female':
            friend.img_url = f'https://avatar.iran.liara.run/public/girl?username={friend.name}'
        else:
            friend.img_url = None

        db.session.commit()
        return jsonify(friend.to_json()),200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400