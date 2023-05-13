import React, { useState, useEffect, useRef } from 'react'
import CanvasDraw from '../components/CanvasDraw';
import '../css/GamePageDrawer.css';
import axios from 'axios';
import IP from '../ip';

export default function GamePageDrawer() {

    const [frase, setFrase] = useState("When I arrive at Londres, I will...");
    const [player, setPlayer] = useState("Jorge");
    const [messages, setMessages] = useState([]);
    const [roomID, setRoomID] = useState();

    const chatRef = useRef(null);

    useEffect(() => {
      const room = localStorage.getItem('roomID');
      setRoomID(room);
      let getChat = async () =>{
        let response = await axios.get(`http://${IP}:5000/room/${roomID}/missatges`);
        if (response.data){
          let momMessages = [];
          for (let i =0; i< response.data.msg.length; i++){
            momMessages.push([response.data.msg[i].player, response.data.msg[i].msg]);
          }
          setMessages(momMessages);
        }
      }
    },[messages]);

  return (
    <div className="GamePageDrawer">
      <div className="BoxSide">
      <h1>{frase}</h1>
        <div id="Canvas">
          <CanvasDraw/>
        </div>

        <h3>Drawing player: {player}</h3>
      </div>

      <div className='ChatSide'>
      <h1>Answers {roomID}</h1>
          {Object.entries(messages).map(([key, value]) => (
            <h3>{key}: {value}</h3>
          ))}
          <input placeholder='Write your guess' one/>
      </div>
      
    </div>
  )
}
