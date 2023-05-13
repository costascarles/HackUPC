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
    const [inputValue, setInputValue] = useState('');

    const chatRef = useRef(null);

    const handleKeyPress = async (event) => {
      let room = localStorage.getItem("roomID");
      if (event.key === 'Enter') {
        console.log("enter pressed"+ event.target.value);
        let response = await axios.post(`http://${IP}:5000/room/${room}/missatges`,{
          "msg": event.target.value,
          "player": localStorage.getItem('username')
        })

        let check = await axios.post(`http://${IP}:5000/room/${room}/check`,{
          "msg": event.target.value,
          "player": localStorage.getItem('username')
        });
        setInputValue(''); // Limpiamos el campo de texto        
      }
    };

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


    useEffect(() => {

      myInterval();
        const room = localStorage.getItem('roomID');
        setRoomID(room);
    },[]);

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
            <h3>{value[0]}: {value[1]}</h3>
          ))}
          <input placeholder='Write your guess' value={inputValue} onChange={(e) => setInputValue(e.target.value)} onKeyUp={(e) => handleKeyPress(e)}/>
      </div>
      
    </div>
  )
}

