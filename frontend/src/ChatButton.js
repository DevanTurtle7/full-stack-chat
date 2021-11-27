import { Component } from 'react';
import { Col } from 'reactstrap';

class ChatButton extends Component {
    onClick = () => {
        console.log("hello")
    }

    render() {
        return (
            <Col onClick={this.onClick} className="chat-button">
                <p>{this.props.name}</p>
                <p>{this.props.lastMessage}</p>
            </Col>
        )
    }
}

export default ChatButton;