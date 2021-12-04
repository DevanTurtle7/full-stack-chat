/**
 * A button on the sidebar that opens a chat
 * 
 * PROPS:
 *  name: The name of this chat. If it is a direct message, the name of the user.
 *  lastMessage: The most recent message that was sent in this chat.
 *  callback: A callback to the parent, that tells it when this button has been clicked.
 * 
 * @author Devan Kavalchek
 */
import { Component } from 'react';
import { Col, Row } from 'reactstrap';

class ChatButton extends Component {
    /**
     * Called when this button is clicked. Calls the callback to the parent
     */
    onClick = () => {
        this.props.callback(this.props.name)
    }

    render() {
        return (
            <Col onClick={this.onClick} className="chat-button">
                <Row>
                    <p>{this.props.name}</p>
                    <p>{this.props.lastSent}</p>
                </Row>
                <p>{this.props.lastMessage}</p>
            </Col>
        )
    }
}

export default ChatButton;