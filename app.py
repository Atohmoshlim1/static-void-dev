from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/')
def home():
    return render_template('home.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/Analysis')
def Analysis():
    return render_template('Analysis.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/About_us')
def About_us():
    return render_template('About_us.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/RRH')
def RRH():
    return render_template('RRH.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/ARH')
def ARH():
    return render_template('ARH.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/dislike_event/<int:event_id>', methods=['POST'])
def dislike_event(event_id):
    event = next((e for e in events if e['id'] == event_id), None)

    if event:
        event['dislikes'] += 1

    return jsonify({'dislikes': event['dislikes']})
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/unlike_event/<int:event_id>', methods=['POST'])
def unlike_event(event_id):
    # Find the event with the given event_id in your data
    event = next((e for e in events if e['id'] == event_id), None)

    if event and event['likes'] > 0:
        # Simulate unliking by decrementing the likes count
        event['likes'] -= 1

    # Return the updated likes count as JSON
    return jsonify({'likes': event['likes']})
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/like_event/<int:event_id>', methods=['POST'])
def like_event(event_id):
    # Find the event with the given event_id in your data
    event = next((e for e in events if e['id'] == event_id), None)

    if event:
        # Increment the likes count
        event['likes'] += 1

    return jsonify({'likes': event['likes']})
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/undislike_event/<int:event_id>', methods=['POST'])
def undislike_event(event_id):
    event = next((e for e in events if e['id'] == event_id), None)

    if event and event['dislikes'] > 0:
        event['dislikes'] -= 1

    return jsonify({'dislikes': event['dislikes']})
events = [
    {
        'id': 1,  # Unique ID for Event 1
        'date': 'today',
        'time': '04:20',
        'user_image': 'https://bootdey.com/img/Content/avatar/avatar1.png',
        'user_name': 'John Smith',
        'location': '795 Folsom Ave, Suite 600 San Francisco, CA 94107',
        'event_name': 'Event 1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'image': 'https://example.com/event_image_1.jpg',
        'likes': 0,
        'dislikes': 0,
        'comments': [],
    },
    {
        'id': 2,  # Unique ID for Event 2
        'date': '24 February 2014',
        'time': '08:17',
        'user_image': 'https://bootdey.com/img/Content/avatar/avatar1.png',
        'user_name': 'Richard Leong',
        'location': '123 Main St, New York, NY 10001',
        'event_name': 'Event 2',
        'description': 'Quisque sed varius nisl. Nulla facilisi.',
        'image': 'https://example.com/event_image_2.jpg',
        'likes': 5,
        'dislikes': 0,
        'comments': [],
    },
    {
        'id': 3,  # Unique ID for Event 3
        'date': '24 February 2014',
        'time': '08:17',
        'user_image': 'https://bootdey.com/img/Content/avatar/avatar1.png',
        'user_name': 'Richard Leong',
        'location': '123 Main St, New York, NY 10001',
        'event_name': 'Event 3',
        'description': 'Quisque sed varius nisl. Nulla facilisi.',
        'image': 'https://example.com/event_image_3.jpg',
        'likes': 0,
        'dislikes': 0,
        'comments': [],
    },
    {
        'id': 5,  # Unique ID for Event 1
        'date': 'today',
        'time': '04:20',
        'user_image': 'https://bootdey.com/img/Content/avatar/avatar1.png',
        'user_name': 'John Smith',
        'location': '795 Folsom Ave, Suite 600 San Francisco, CA 94107',
        'event_name': 'Event 15',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'image': 'https://example.com/event_image_1.jpg',
        'likes': 0,
        'dislikes': 0,
        'comments': [],
    },
    {
        'id': 6,  # Unique ID for Event 2
        'date': '24 February 2014',
        'time': '08:17',
        'user_image': 'https://bootdey.com/img/Content/avatar/avatar1.png',
        'user_name': 'Richard Leong',
        'location': '123 Main St, New York, NY 10001',
        'event_name': 'Event 33',
        'description': 'Quisque sed varius nisl. Nulla facilisi.',
        'image': 'https://example.com/event_image_2.jpg',
        'likes': 5,
        'dislikes': 0,
        'comments': [],
    },
    {
        'id': 7,  # Unique ID for Event 3
        'date': '24 February 2014',
        'time': '08:17',
        'user_image': 'https://bootdey.com/img/Content/avatar/avatar1.png',
        'user_name': 'Richard Leong',
        'location': '123 Main St, New York, NY 10001',
        'event_name': 'Event 34',
        'description': 'Quisque sed varius nisl. Nulla facilisi.',
        'image': 'https://example.com/event_image_3.jpg',
        'likes': 0,
        'dislikes': 0,
        'comments': [],
        
    }
    
    
    # Add more events as needed
]
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/Events')
def Events():
    return render_template('events.html', events=events)
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/Post')
def post_event():
    
    return  render_template('Post.html')
#---------------------------------------------------------------------------------------------------------------------------------------   
@app.route('/Requst_Ride')
def requst_ride():
    # Retrieve the URL parameters
    dropoff_location = request.args.get('dropoff')
    comments = request.args.get('comments')

    # Pass these parameters to your template for pre-filling
    return render_template('Requst_Ride.html', dropoff=dropoff_location, comments=comments)
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/Accept_Ride')
def Accept_Ride():
    rides = [
        {
            'id': 1,
            'user_name': 'User 1',
            'event_name': 'Event 1',
            'from_location': 'Location A',
            'to_location': 'Location B',
            'num_seats': 3,
            'time': '04:20',  # Add the time attribute
        },
        {
            'id': 2,
            'user_name': 'User 2',
            'event_name': 'Event 2',
            'from_location': 'Location C',
            'to_location': 'Location D',
            'num_seats': 2,
            'time': '08:00',  # Add the time attribute
        },
        {
            'id': 3,
            'user_name': 'User 3',
            'event_name': 'Event 3',
            'from_location': 'Location E',
            'to_location': 'Location F',
            'num_seats': 1,
            'time': '12:45',  # Add the time attribute
        },
        # Add more rides as needed
    ]

    return render_template('Accept_Ride.html', rides=rides)
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/EH')
def EH():
    return render_template('EH.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/Profile')
def Profile():
    return render_template('Profile.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/UpdateProfile')
def UpdateProfile():
    return render_template('UpdateProfile.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/SISU')
def SISU():
    return render_template('SISU.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/signup')
def signup():
    return render_template('signup.html')
#---------------------------------------------------------------------------------------------------------------------------------------
@app.route('/f_pass')
def f_pass():
    return render_template('f_pass.html')
#---------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)