import React, { useState, useEffect } from 'react'
import CanvasDraw from '../components/CanvasDraw';
import '../css/GamePageDrawer.css';

export default function GamePageDrawer() {

    const [frase, setFrase] = useState("When I arrive at Londres, I will...");
    const [player, setPlayer] = useState("Jorge");
    const [messages, setMessages] = useState({
      "pepe": "FRASEE1",
      "eric": "FRASEEEE2",
      "jose": "FRASEE3",
      "luis": "FRAS E E E E 4",
      "marta": "FRA S EE  5",
      "mario": "FRASEEEE6",
    });
  return (
    <div className="GamePage">
      <div className="BoxSide">
        <h1>{frase}</h1>
        <div id="Canvas">
          <CanvasDraw/>
        </div>

        <h3>Drawing player: {player}</h3>
      </div>

      <div className='ChatSide'>
          {Object.entries(messages).map(([key, value]) => (
            <h3>{key}: {value}</h3>
          ))}
      </div>
      
    </div>
  )
}
