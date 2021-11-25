import './App.css';
import Chat from './Chat';
import Sidebar from './Sidebar';
import { Row, Container } from 'reactstrap';

function App() {
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

export default App;
