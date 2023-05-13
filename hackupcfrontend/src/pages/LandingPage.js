import React from 'react'
//import axios from 'axios';
import '../css/landingPage.css';
import vuelingLogo from '../styles/Logo_Vueling.svg.png';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation, useNavigate } from 'react-router-dom';
import IP from '../ip';

export default function LandingPage() {

  const [players, setPlayers] = useState([]);
  const [waiting, setWaiting] = useState('Waiting for players');
  const [rendered, setRendered] = useState(false);
  const [roomID, setRoomID] = useState();
  const navigation = useNavigate();

  const handlePlayers = async () => {

  }

  
  const handleGame = async () => {
    let response = await axios.post(`http://${IP}:5000/room/${roomID}/selectDrawer`,{
      'room_id': roomID
    });

    let response2 = await axios.get(`http://${IP}:5000/room/${roomID}`);
    let pl = response2.data.players
    for (let i = 0; i<pl.length; i++){
      if (pl.dibujar == true && pl.nombre == localStorage.getItem('username')){
        navigation("/selectionFrase");
      } else {
        navigation("/gameAnswer");
      }
    }   
  }

  useEffect(() => {
    const room = localStorage.getItem('roomID');
    setRoomID(room);
    let getPlayers = async () => {
      try {
        let response = await axios.get(`http://${IP}:5000/room/${room}`);
        if (response.data) {
          setPlayers(response.data.players);
          console.log(response.data);
          setRendered(true);
        }
      } catch (error){
        //stuff
      }
    }
    setTimeout(async ()=>{
      await getPlayers();
    },5000);
  }, []);

  useEffect(()=>{
    setTimeout("",1000);
    setTimeout(()=>{
      if (waiting.length != 22){
        setWaiting(waiting + '.');
      } else{
        setWaiting("Waiting for players");
      }
    }, 700);
  })


  return (
    <div className='landingPage'>
      <h1>Flying to the new game</h1>
      <h3>{waiting}</h3>
      <button onClick={(e) => handleGame(e)}>Start game</button>
      
      {
        players && 
      <table>
        {
          rendered && (
            <>
              <tr>
                <td>{players[0] ? players[0].nombre : "Waiting for player"}</td>
                <td>{players[1] ? players[1].nombre : "Waiting for player"}</td>
                <td>{players[2] ? players[2].nombre : "Waiting for player"}</td>
                <td>{players[3] ? players[3].nombre : "Waiting for player"}</td>
              </tr>
              <tr>
                <td>{players[4] ? players[4].nombre : "Waiting for player"}</td>
                <td>{players[5] ? players[5].nombre : "Waiting for player"}</td>
                <td>{players[6] ? players[6].nombre : "Waiting for player"}</td>
                <td>{players[7] ? players[7].nombre : "Waiting for player"}</td>
              </tr>
       
            </>
          )
        }
        
      </table>
      }
      <img src={vuelingLogo} id='logoVueling'/>
    </div>
  )
}
