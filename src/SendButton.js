import { Component } from 'react';
import { Col, Button } from 'reactstrap';
import { MdAdd } from "react-icons/md";

class SendButton extends Component {
    render() {
        return (
            <Col md="auto" className="px-2">
                <Button color="primary">
                    <MdAdd />
                </Button>
            </Col>
        )
    }
}

export default SendButton;