import { Component } from 'react';
import { Row } from 'reactstrap';
import SendButton from './SendButton';
import MessageInput from './MessageInput';

class ChatInput extends Component {
    render() {
        return (
            <div className="chat-input position-fixed end-0 bottom-0">
                <Row className="mx-2 mb-2">
                    <MessageInput />
                    <SendButton />
                </Row>
            </div>
        )
    }
}

export default ChatInput;