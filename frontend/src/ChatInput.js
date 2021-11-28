import { Component } from 'react';
import { Row } from 'reactstrap';
import SendButton from './SendButton';
import MessageInput from './MessageInput';

const API_URL = 'http://127.0.0.1:5000'

class ChatInput extends Component {
    constructor(props) {
        super(props)
        this.state = {
            message: ""
        }

        this.userId = 1
    }

    sendMessage = () => {
        let current = this.props.current
        let type = current.type
        let id = current.id
        let route;
        let body = {
            'user_id': this.userId,
            'text': this.state.message
        }

        if (type === 'direct_message') {
            route = '/direct_messages'
            body['receiver_id'] = id
        } else if (type === 'group_chat') {
            route = '/group_messages'
            body['group_chat_id'] = id
        }

        fetch(API_URL + route, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        }).then(response => response.json())
            .then(response => {
                if (response.success) {
                    this.setState({message: ''})
                    this.props.refreshApp();
                }
            });
    }

    updateMessage = (newMessage) => {
        this.setState({ message: newMessage })
    }

    render() {
        return (
            <div className="chat-input position-fixed end-0 bottom-0">
                <Row className="m-2 mt-4">
                    <MessageInput callback={this.updateMessage} text={this.state.message} sendMessage={this.sendMessage}/>
                    <SendButton callback={this.sendMessage} />
                </Row>
            </div>
        )
    }
}

export default ChatInput;