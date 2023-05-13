import React from 'react'
import '../css/Lobby.css'

export default function Lobby({name, numPlayers}) {
  return (
    <div className='Lobby'>
        <h1>Lobby: {name}</h1>
        <h3>Players: {numPlayers}</h3>
    </div>
  )
}
