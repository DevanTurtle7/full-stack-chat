import { Component } from 'react';
import { Row } from 'reactstrap';
import SendButton from './SendButton';
import MessageInput from './MessageInput';

class ChatInput extends Component {
    constructor(props) {
        super(props)
        this.state = {
            message: ""
        }
    }

    sendMessage = () => {
        console.log('sending message: ' + this.state.message)
    }

    updateMessage = (newMessage) => {
        this.setState({ message: newMessage })
    }

    render() {
        return (
            <div className="chat-input position-fixed end-0 bottom-0">
                <Row className="m-2 mt-4">
                    <MessageInput callback={this.updateMessage}/>
                    <SendButton callback={this.sendMessage}/>
                </Row>
            </div>
        )
    }
}

export default ChatInput;