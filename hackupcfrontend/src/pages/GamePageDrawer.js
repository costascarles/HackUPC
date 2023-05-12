import React, { useState } from 'react'

export default function GamePageDrawer() {

    const [frase, setFrase] = useState("");
    const [player, setPlayer] = useState("");
  return (
    <div className="GamePage">
      <div className="BoxSide">
        <h1></h1>
      </div>

      <div className='ChatSide'>

      </div>
      
    </div>
  )
}
