/**
 * A chat bubble that is displayed in a chat
 * 
 * PROPS:
 *  sent: A boolean value. True if the current user sent this message. False otherwise.
 *  text: The text of the current message that is displayed in this bubble
 *  first: A boolean value. True if this is the first message of a block of messages:
 *        a series of consecutive messages from the same sender. True if the message
 *        before this was sent by the same person, or if there are no messages before
 *        this. False otherwise.
 *  last: A boolean value. True if this is the last message of a block of messages:
 *        a series of consecutive messages from the same sender. True if the message
 *        after this was sent by the same person, or if there are no messages after
 *        this. False otherwise. 
 * 
 * @author Devan Kavalchek
 */

import { Component } from 'react';
import {
    Col,
} from 'reactstrap';

class Bubble extends Component {
    render() {
        // Determine the accurate class names for bubble styling
        let sentClassName = this.props.sent ? "chat-bubble-sent" : "chat-bubble-received";
        let firstClassName = this.props.first ? "chat-bubble-first" : ""
        let lastClassName = this.props.last ? "chat-bubble-last" : ""
        let justification = this.props.sent ? "justify-content-end" : "justify-content-start"
        let bgColor = this.props.sent ? "bg-primary" : "bg-secondary"

        return (
            <Col className={"d-flex " + justification}>
                <div className={"chat-bubble "
                    + sentClassName + " "
                    + firstClassName + " "
                    + lastClassName + " "
                    + bgColor}>
                    <p>{this.props.text}</p>
                </div>
            </Col>
        )
    }
}

export default Bubble;