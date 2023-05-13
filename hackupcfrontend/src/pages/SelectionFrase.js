import React, { useEffect, useState } from 'react'
import axios from 'axios';
import IP from '../ip';
import { useNavigate } from 'react-router-dom';

export default function SelectionFrase() {
    const [frase, setFrase] = useState("");
    const [roomID, setRoomID] = useState();
    const navigator = useNavigate();

    const handleSubmit = async (e) =>{
        e.preventDefault();
        let fraseEncertar = e.target.value;
        setFrase(frase + fraseEncertar);

        let response = await axios.post(`http://${IP}/room/${roomID}/fixFrase`,{
            text: fraseEncertar
        });
        navigator("/gameDrawer");
    }

    useEffect(()=>{
        let room = localStorage.getItem('roomID');
        setRoomID(room);
        let getFrase = async () =>{
            let response = await axios.get(`http://${IP}/room/${room}/frase`);
            setFrase(response.data.frase);
        }
    }, []);

  return (
    <div>
        <h1>{frase}</h1>
        <input placeholder='Fill the gap'></input>
        <button type='submit' onSubmit={(e) => handleSubmit(e)}></button>
    </div>
  )
}
