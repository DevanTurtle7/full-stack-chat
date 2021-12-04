import { Component } from 'react';
import { Col } from 'reactstrap';
import ChatButton from './ChatButton';

class Sidebar extends Component {
    render() {
        let buttons = []

        for (var key in this.props.chats) {
            let chat = this.props.chats[key]

            buttons.push(<ChatButton
                name={chat.name}
                lastMessage={chat.last_message}
                lastSent={chat.last_sent}
                callback={this.props.callback}
                key={key}
            />)
        }

        return (
            <Col sm={4} className="sidebar">
                {buttons}
            </Col>
        )
    }
}

export default Sidebar;