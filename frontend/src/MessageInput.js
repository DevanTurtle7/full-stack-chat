import { Component } from 'react';
import { Col, Input } from 'reactstrap';

class MessageInput extends Component {
    onChange = (event) => {
        this.props.callback(event.target.value)
    }

    render() {
        return (
            <Col className="px-0">
                <Input className="message-input" placeholder="Text message" defaultValue="" onChange={this.onChange}/>
            </Col>
        )
    }
}

export default MessageInput;