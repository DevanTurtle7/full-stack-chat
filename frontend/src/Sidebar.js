import { Component } from 'react';
import { Col } from 'reactstrap';
import ChatButton from './ChatButton';

class Sidebar extends Component {
    render() {
        return (
            <Col sm={4} className="sidebar">
                <ChatButton/>
            </Col>
         )
    }
}

export default Sidebar;