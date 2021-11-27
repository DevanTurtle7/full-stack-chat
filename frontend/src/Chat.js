import { Component } from 'react';
import { Col } from 'reactstrap';
import Bubble from './Bubble';
import ChatInput from './ChatInput';

const API_URL = 'http://127.0.0.1:5000'

class Chat extends Component {
    constructor(props) {
        super(props)

        this.state = {
            messages: []
        }
        this.userId = 1;
    }

    getMessages = () => {
        let current = this.props.current

        if (current != null) {
            let type = current['type']
            let id = current['id']
            let route;

            if (type === 'direct_message') {
                route = `/direct_messages?user_id=${this.userId}&receiver_id=${id}`
            } else if (type === 'group_chat') {
                route = `/group_messages?user_id=${this.userId}&group_chat_id=${id}`
            }

            fetch(API_URL + route, {
                method: 'GET',
            }).then(response => response.json())
                .then(response => {
                    this.setState({ messages: response })
                });
        } else {
            this.setState({ messages: [] })
        }
    }

    componentDidMount() {
        this.getMessages()
    }

    componentDidUpdate(prevProps) {
        if (prevProps !== this.props) {
            this.getMessages()
        }
    }

    render() {
        var messages = this.state.messages
        var numMessages = messages.length
        var bubbles = []

        for (var i = 0; i < numMessages; i++) {
            let message = messages[i]
            let sender = message.sender_id

            bubbles.push(<Bubble
                sent={sender === this.userId}
                text={message.message_text}
                first={i === 0 || messages[i - 1].sender_id !== sender}
                last={i === (numMessages - 1) || messages[i + 1].sender_id !== sender}
                key={i}
            />)
        }

        if (this.props.current === null) {
            return (
                <Col sm={8} className="chat-window">
                    {bubbles}
                </Col>
            )
        } else {
            return (
                <Col sm={8} className="chat-window">
                    {bubbles}
                    <ChatInput />
                </Col>
            )
        }
    }
}

export default Chat;