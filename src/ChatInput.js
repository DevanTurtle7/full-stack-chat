import { Component } from 'react';
import { Col, Input, Row } from 'reactstrap';
import SendButton from './SendButton';

class ChatInput extends Component {
    render() {
        return (
            <div className="chat-input position-fixed end-0 bottom-0">
                <Row className="mx-2 mb-2">
                    <Col className="px-0">
                        <Input/>
                    </Col>
                    <SendButton />
                </Row>
            </div>
        )
    }
}

export default ChatInput;