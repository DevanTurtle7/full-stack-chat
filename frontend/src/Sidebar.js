import { Component } from 'react';
import { Col } from 'reactstrap';
import ChatButton from './ChatButton';

class Sidebar extends Component {
    render() {
        let buttons = []
        console.log(this.props.chats)

        if (this.props.chats.length > 0) {
            for (var i = 0; i < this.props.chats.length; i++) {
                let chat = this.props.chats[i]

                buttons.push(<ChatButton
                    name={chat.name}
                    lastMessage={chat.last_message}
                    key={i}
                />)
            }
        }

        return (
            <Col sm={4} className="sidebar">
                {buttons}
            </Col>
        )
    }
}

export default Sidebar;