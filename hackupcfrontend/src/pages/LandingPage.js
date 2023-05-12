import React from 'react'
import axios from 'axios';
import '../styles/landingPage.css';
import vuelingLogo from '../styles/Logo_Vueling.svg.png';

import { useState, useEffect } from 'react';

export default function LandingPage() {

  const [players, setPlayers] = useState([]);
  const [waiting, setWaiting] = useState('Waiting for players');

  const handlePlayers = async () => {

  }

  useEffect(() => {
    /*
    let getPlayers = async () => {
      try {
        let players = await axios.get('ip');
        if (players.data.size) {
          setPlayers(players);
        }
      } catch (error){
        //stuff
      }
    }
    getPlayers();
    */
  });

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
      
      <table>
        <tr>
          <td>PLAYER1</td>
          <td>PLAYER2</td>
          <td>PLAYER3</td>
          <td>PLAYER4</td>
        </tr>
        <tr>
          <td>PLAYER5</td>
          <td>PLAYER6</td>
          <td>PLAYER7</td>
          <td>PLAYER8</td>
        </tr>
      </table>
      <img src={vuelingLogo} id='logoVueling'/>
    </div>
  )
}
