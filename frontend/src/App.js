import './App.css';
import Chat from './Chat';
import Sidebar from './Sidebar';
import { Row, Container } from 'reactstrap';
import { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      open: null,
    }
  }

  render() {
    return (
      <div className="App">
        <Container fluid>
          <Row className="row-height">
            <Sidebar />
            <Chat />
          </Row>
        </Container>
      </div>
    );
  }
}

export default App;
