import { Component } from 'react';
import {
    Col,
    Container
} from 'reactstrap';

class Bubble extends Component {
    constructor(props) {
        super(props);

        this.sentClassName = this.props.sent ? "chatBubble-sent" : "chatBubble-received";
        this.justification = this.props.sent ? "justify-content-end" : "justify-content-start"
    }

    render() {
        return (
            <Col className={"d-flex " + this.justification}>
                <div className={"chatBubble " + this.sentClassName}>
                    <p>{this.props.text}</p>
                </div>
            </Col>
        )
    }
}

export default Bubble;