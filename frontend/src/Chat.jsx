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
import { useCallback, useEffect, useState } from 'react';
import { Col } from 'reactstrap';
import Bubble from './Bubble';
import ChatInput from './ChatInput';

function Chat(props) {
    const [messages, setMessages] = useState([])
    const [current, setCurrent] = useState(null)
    const userId = 1;

    /**
     * Gets all the messages of the chat from the API
     */
    const getMessages = useCallback(() => {
        let current = props.current

        if (current !== null) {
            let type = current.type
            let id = current.id
            let route;

            // Generate the route, depending on if the chat is a group chat or a direct message
            if (type === 'direct_message') {
                route = `/direct_messages?user_id=${userId}&receiver_id=${id}`
            } else if (type === 'group_chat') {
                route = `/group_messages?user_id=${userId}&group_chat_id=${id}`
            }

            // Make a call to the api to get the messages
            fetch(route, {
                method: 'GET',
            }).then(response => response.json())
                .then(response => {
                    setMessages([...response])
                });
        } else {
            setMessages([])
        }
    }, [props, setMessages])

    useEffect(() => {
        if (props.current !== current) {
            getMessages()
            setCurrent(props.current)
            console.log(1)
        }
    }, [setCurrent, current, getMessages, props])

    /**
     * Refreshes the entire app. Used by the send button
     */
    const refreshApp = () => {
        props.refreshApp(userId)
    }

    const getBubbles = () => {
        const numMessages = messages.length
        const bubbles = []

        // Dynamically render bubbles
        for (var i = numMessages - 1; i >= 0; i--) { // Iterate backwords over the messages (oldest to newest)
            let message = messages[i] // Get the current message
            let sender = message.sender_id
            // Determine the props
            let sent = sender === userId
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

        return bubbles
    }

    if (props.current === null) {
        return (<Col sm={8} className="chat-window"></Col>)
    } else {
        return (
            <Col sm={8} className="chat-window">
                {getBubbles()}
                <ChatInput current={props.current} refreshApp={refreshApp} />
            </Col>
        )
    }
}

export default Chat;