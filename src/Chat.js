import { Component } from 'react';
import { Col } from 'reactstrap';
import Bubble from './Bubble';

class Chat extends Component {
    render() {
        return (
            <Col className="mx-1">
                <Bubble sent={true} text={"Hello"}/>
                <Bubble sent={true} text={"This is a long message. This is a test to see what a long message looks like. Lets try it out."}/>
                <Bubble sent={false} text={"Hey whats up. This is a long message from the other user."}/>
            </Col>
        )
    }
}

export default Chat;