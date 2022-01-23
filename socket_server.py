import socketio

# create a Socket.IO server
sio = socketio.Server(cors_allowed_origins='*')

# wrap with a WSGI application
app = socketio.WSGIApp(sio)


@sio.on('data')
def get_data(sid, data):
    print(data)