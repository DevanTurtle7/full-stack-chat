import './App.css';
import Chat from './Chat';
import Sidebar from './Sidebar';
import { Row } from 'reactstrap';

function App() {
  return (
    <div className="App">
      <Row>
        <Sidebar />
        <Chat />
      </Row>
    </div>
  );
}

export default App;
