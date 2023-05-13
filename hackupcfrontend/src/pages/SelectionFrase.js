import React, { useEffect, useState } from 'react'
import axios from 'axios';
import IP from '../ip';
import { useNavigate } from 'react-router-dom';

export default function SelectionFrase() {
    const [frase, setFrase] = useState("");
    const [roomID, setRoomID] = useState();
    const navigator = useNavigate();
    const [text, setText] =useState("");

    const handleClick = async (e) =>{
        //e.preventDefault();
        console.log(text);
        let response = await axios.post(`http://${IP}:5000/room/${roomID}/fixFrase`,{
            "text": text
        });
        console.log(response);
        navigator("/gameDrawer");
    }

    useEffect(()=>{
        let room = localStorage.getItem('roomID');
        console.log(room); 
        setRoomID(room);
        let getFrase = async () =>{
            let response = await axios.get(`http://${IP}:5000/room/${room}/frase`);
            setFrase(response.data.frase);
        }
        getFrase();
    }, []);

  return (
    <div>
        <h1>{frase}</h1>
        <input placeholder='Fill the gap' onChange={e => setText(e.target.value)}></input>
        <button type='submit' onClick={(e) => handleClick(e)}>Submit</button>
    </div>
  )
}
