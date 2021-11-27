import { Component } from 'react';
import { Col, Button } from 'reactstrap';
import { MdSend } from "react-icons/md";

class SendButton extends Component {
    onClick = () => {
        this.props.callback()
    }

    render() {
        return (
            <Col md="auto" className="px-2">
                <Button color="primary" className="circular-btn" onClick={this.onClick}>
                    <MdSend color="white"/>
                </Button>
            </Col>
        )
    }
}

export default SendButton;