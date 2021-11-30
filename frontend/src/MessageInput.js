import { Component } from 'react';
import { Col, Input } from 'reactstrap';

class MessageInput extends Component {
    onChange = (event) => {
        this.props.callback(event.target.value)
    }

    onKeyPress = (event) => {
        if (event.charCode === 13) {
            this.props.sendMessage()
        }
    }

    render() {
        return (
            <Col className="px-0">
                <Input
                    className="message-input"
                    placeholder="Text message"
                    value={this.props.text}
                    onChange={this.onChange}
                    onKeyPress={this.onKeyPress}
                />
            </Col>
        )
    }
}

export default MessageInput;