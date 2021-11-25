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
            {sender: 1, message: "This is a long message. This is a test to see what a long message looks like. Lets try it out."},
            {sender: 2, message: "Hey whats up. This is a long message from the other user"}
        ]
        
        this.userId = 1;
    }

    render() {
        var messages = []

        for (var i in this.messages) {
            let message = this.messages[i]

            messages.push(<Bubble
                sent={message.sender === this.userId}
                text={message.message}
            />)
        }

        return (
            <Col className="mx-1">{messages}</Col>
        )
    }
}

export default Chat;