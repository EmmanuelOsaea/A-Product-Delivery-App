const roomName = 'order123';
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
  );

chatSocket.onmessage=function(e) {
    const data = JSON.parse(e.data);
    console.log('Received message:', data.message);
};

chatSocket.onopen = function(e) {
  chatSocket.send(JSON.stringify({'message': 'Hello from client!'}));
};
