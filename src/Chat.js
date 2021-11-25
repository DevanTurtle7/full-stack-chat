import { Component } from 'react';
import { Col } from 'reactstrap';
import Bubble from './Bubble';

class Chat extends Component {
    constructor(props) {
        super(props)

        // Temp stuff for testing
        this.messages = [
            {sender: 1, message: "hello"},
            {sender: 1, message: "Lorem ipsum..."},
            {sender: 1, message: "Blah blah blah"},
            {sender: 1, message: "This is a long message. This is a test to see what a long message looks like. Lets try it out."},
            {sender: 2, message: "Hey whats up. This is a long message from the other user"},
            {sender: 2, message: "This is another random message from the other person"},
            {sender: 1, message: "Okay bye"},
        ]
        
        this.userId = 1;
    }

    render() {
        var messages = []
        var numMessages = this.messages.length

        for (var i = 0; i < numMessages; i++) {
            let message = this.messages[i]
            let sender = message.sender

            messages.push(<Bubble
                sent={sender === this.userId}
                text={message.message}
                first={i === 0 || this.messages[i-1].sender !== sender}
                last={i === (numMessages - 1) || this.messages[i+1].sender !== sender}
                key={i}
            />)
        }

        return (
            <Col className="mx-1">{messages}</Col>
        )
    }
}

export default Chat;