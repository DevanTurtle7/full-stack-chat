/**
 * A chat window
 * 
 * PROPS:
 *  current: A JSON object representing the chat that is currently being displayed.
 *  refreshApp: A function that triggers the entire app to refresh. This function
 *              is used by the send button to trigger a refresh after a new message
 *              was succesfully sent.
 * 
 * @author Devan Kavalchek
 */
import { Component } from 'react';
import { Col } from 'reactstrap';
import Bubble from './Bubble';
import ChatInput from './ChatInput';

class Chat extends Component {
    constructor(props) {
        super(props)

        this.state = {
            messages: []
        }

        this.userId = 1;
    }
    
    /**
     * Gets all the messages of the chat from the API
     */
    getMessages = () => {
        let current = this.props.current

        if (current !== null) {
            let type = current.type
            let id = current.id
            let route;

            // Generate the route, depending on if the chat is a group chat or a direct message
            if (type === 'direct_message') {
                route = `/direct_messages?user_id=${this.userId}&receiver_id=${id}`
            } else if (type === 'group_chat') {
                route = `/group_messages?user_id=${this.userId}&group_chat_id=${id}`
            }

            // Make a call to the api to get the messages
            fetch(route, {
                method: 'GET',
            }).then(response => response.json())
                .then(response => {
                    this.setState({ messages: response })
                });
        } else {
            this.setState({ messages: [] })
        }
    }

    componentDidUpdate(prevProps) {
        // Get the messages anytime there is an update
        if (prevProps !== this.props) {
            this.getMessages()
        }
    }

    componentDidMount() {
        // Get the messages the first time the object is created
        this.getMessages()
    }

    /**
     * Refreshes the entire app. Used by the send button
     */
    refreshApp = () => {
        this.props.refreshApp(this.userId)
    }

    render() {
        let messages = this.state.messages
        let numMessages = messages.length
        const bubbles = []

        // Dynamically render bubbles
        for (var i = numMessages - 1; i >= 0; i--) { // Iterate backwords over the messages (oldest to newest)
            let message = messages[i] // Get the current message
            let sender = message.sender_id
            // Determine the props
            let sent = sender === this.userId
            let text = message.message_text
            let first = i === (numMessages - 1) || messages[i + 1].sender_id !== sender
            let last = i === 0 || messages[i - 1].sender_id !== sender

            // Add a new bubble
            bubbles.push(<Bubble
                sent={sent}
                text={text}
                first={first}
                last={last}
                key={i}
            />)
        }

        if (this.props.current === null) {
            return (<Col sm={8} className="chat-window"></Col>)
        } else {
            return (
                <Col sm={8} className="chat-window">
                    {bubbles}
                    <ChatInput current={this.props.current} refreshApp={this.refreshApp}/>
                </Col>
            )
        }
    }
}

export default Chat;