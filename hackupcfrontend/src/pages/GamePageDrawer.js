import React, { useState, useEffect, useRef } from 'react'
import CanvasDraw from '../components/CanvasDraw';
import '../css/GamePageDrawer.css';
import axios from 'axios';
import IP from '../ip';

export default function GamePageDrawer() {

    const [frase, setFrase] = useState(localStorage.getItem("frase"));
    const [player, setPlayer] = useState("Jorge");
    const [messages, setMessages] = useState([]);
    const [roomID, setRoomID] = useState();

    const chatRef = useRef(null);

    useEffect(() => {
      myInterval();
        const room = localStorage.getItem('roomID');
        setRoomID(room);
    },[]);

    const myInterval = () =>{
      let interval = setInterval(()=>{
        getChat();
      },3500);
    }

    const getChat = async () =>{
      let room = localStorage.getItem("roomID");
      let response = await axios.get(`http://${IP}:5000/room/${room}/missatges`);
      if (response.data){
        let momMessages = [];
        for (let i =0; i< response.data.mensajes.length; i++){
          momMessages.push([response.data.mensajes[i].player, response.data.mensajes[i].msg]);
        }
        setMessages(momMessages);
      }
    }

  return (
    <div className="GamePageDrawer">
      <div className="BoxSide">
      <h1>{frase}</h1>
        <div id="Canvas">
          <CanvasDraw/>
        </div>
      </div>

      <div className='ChatSide'>
      <h1>Answers {roomID}</h1>
          {Object.entries(messages).map(([key, value]) => (
            <h3>{value[0]}: {value[1]}</h3>
          ))}
      </div>
      
    </div>
  )
}
