import { Component } from 'react';
import { Col } from 'reactstrap';

class ChatButton extends Component {
    onClick = () => {
        console.log("hello")
    }

    render() {
        return (
            <Col onClick={this.onClick} className="chat-button">
                <p>User1</p>
                <p>Okay bye</p>
            </Col>
        )
    }
}

export default ChatButton;