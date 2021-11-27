import './App.css';
import Chat from './Chat';
import Sidebar from './Sidebar';
import { Row, Container } from 'reactstrap';
import { Component } from 'react';

const API_URL = 'http://127.0.0.1:5000'

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      open: null,
      chats: {},
      current: null
    }
  }

  getChats = (user_id) => {
    let route = `/chats?user_id=${user_id}`

    fetch(API_URL + route, {
      method: 'GET',
    }).then(response => response.json())
      .then(response => {
        let chats = {}

        for (var i = 0; i < response.length; i++) {
          let current = response[i]

          chats[current.name] = current
        }

        this.setState({ chats: chats })
      });
  }

  componentDidMount() {
    this.getChats(1)
  }

  changeChat = (newChat) => {
    this.setState({ current: this.state.chats[newChat] })
  }

  render() {
    return (
      <div className="App">
        <Container fluid>
          <Row className="row-height">
            <Sidebar chats={this.state.chats} callback={this.changeChat} />
            <Chat current={this.state.current} />
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;
