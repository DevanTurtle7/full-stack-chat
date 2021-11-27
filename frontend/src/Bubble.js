import { Component } from 'react';
import {
    Col,
} from 'reactstrap';

class Bubble extends Component {
    constructor(props) {
        super(props);
    }

    render() {
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