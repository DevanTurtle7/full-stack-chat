import { Component } from 'react';
import { Col, Input } from 'reactstrap';

class MessageInput extends Component {
    render() {
        return (
            <Col className="px-0">
                <Input className="message-input"/>
            </Col>
        )
    }
}

export default MessageInput;