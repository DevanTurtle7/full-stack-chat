import './App.css';
import Chat from './Chat';
import Sidebar from './Sidebar';
import { Row, Container } from 'reactstrap';
import { Component, useEffect, useState } from 'react';

const UPDATE_INTERVAL = 3000

function App(props) {
    const [open, setOpen] = useState(null)
    const [chats, setChats] = useState({})
    const [current, setCurrent] = useState(null)
    const [messages, setMessages] = useState([])
    const [setUp, setSetUp] = useState(false)

    const userId = 1;

    useEffect(() => {
        if (!setUp) {
            getChats(userId)
        }

        const interval = setInterval(() => {
            getChats(userId)
        }, UPDATE_INTERVAL)

        return () => clearInterval(interval)
    })

    const getChats = (user_id) => {
        let route = `/chats?user_id=${user_id}`

        fetch(route, {
            method: 'GET',
        }).then(response => response.json())
            .then(response => {
                let newChats = {}

                for (var i = 0; i < response.length; i++) {
                    let current = response[i]

                    newChats[current.name] = current
                }

                setChats(...[newChats])
                setSetUp(true)
            });
    }

    const changeChat = (newChat) => {
        setCurrent(chats[newChat])
    }

    return (
        <div className="App">
            <Container fluid>
                <Row className="row-height">
                    <Sidebar chats={chats} callback={changeChat} />
                    <Chat current={current} refreshApp={getChats} />
                </Row>
            </Container>
        </div>
    );
}

export default App;
