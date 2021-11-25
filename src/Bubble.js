import { Component } from 'react';
import {
    Col,
} from 'reactstrap';

class Bubble extends Component {
    constructor(props) {
        super(props);

        this.sentClassName = this.props.sent ? "chat-bubble-sent" : "chat-bubble-received";
        this.firstClassName = this.props.first ? "chat-bubble-first" : ""
        this.lastClassName = this.props.last ? "chat-bubble-last" : ""
        this.justification = this.props.sent ? "justify-content-end" : "justify-content-start"
        this.bgColor = this.props.sent ? "bg-primary" : "bg-secondary"
    }

    render() {
        return (
            <Col className={"d-flex " + this.justification}>
                <div className={"chat-bubble "
                + this.sentClassName + " "
                + this.firstClassName + " "
                + this.lastClassName + " "
                + this.bgColor}
                color={this.color}>
                    <p>{this.props.text}</p>
                </div>
            </Col>
        )
    }
}

export default Bubble;