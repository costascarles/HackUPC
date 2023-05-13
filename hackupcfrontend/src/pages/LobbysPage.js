import React, { useEffect, useState } from 'react'
import axios from 'axios';
import Lobby from '../components/Lobby';
import '../css/LobbysPage.css';
import { useNavigate  } from 'react-router-dom';
import vuelingLogo from '../styles/Logo_Vueling.svg.png';
import IP from '../ip';

export default function LobbysPage() {

    const [username, setUsername] = useState("Write your username");
    const [lobbys, setLobbys] = useState([]);
    const navigation = useNavigate();

    const handleUser = async (e) => {
        setUsername(e.target.value);
    }


    const handleCreateRoom = async () =>{
        if (username != "" && username !== "Write your username"){
            try {
                let response = await axios.post(`http://${IP}:5000/connect`, {
                    'username': username,
                    'room': 0
                });
                if (response.data){
                    localStorage.setItem('roomID', 1);
                    localStorage.setItem('username', username);
                    navigation("/landing");
                }
            } catch (error){
                alert(error.message);
            }
        }
    }

    useEffect(() => {
        let getLobbys = async () =>{
            try{
                let response = await axios.get(`http://${IP}:5000/rooms`);
                if (response.data) {
                    setLobbys(response.data);
                    console.log(response.data);
                }
            } catch {
                alert("RIP");
            }
        }
        getLobbys();
    }, []);

    useEffect(()=>{
        if (username === ""){
            setUsername("Write your username");
        }
    }, [username]);


    const handleClick = async (e,lobbyID, numPlayers) => {
        if (numPlayers != 8 && username != "" && username !== "Write your username"){
            try {
                let response = await axios.post(`http://${IP}:5000/connect`, {
                    username: username,
                    room: lobbyID
                });
                alert(lobbyID);
                if (response.data){
                    localStorage.setItem('roomID', lobbyID);
                    localStorage.setItem('username', username);
                    navigation("/landing");
                }
            } catch (error){
                alert(error.message);
            }
        }
    }

  return (
    <div className='lobbysPage'>
        <input placeholder={username} onChange={(e) => handleUser(e)} className='inputName'></input>
        <div className='lobbysList'>
        {
            lobbys.map((lobby) => (
                <div key={lobby.id} onClick={e => handleClick(e, lobby.id, lobby.numPlayers)}>
                    <Lobby name={lobby.id} numPlayers={lobby.numPlayers}/>
                </div>
            ))
        }
        </div>
            <button onClick={(e) => handleCreateRoom(e)}>Create Room</button>
            <img src={vuelingLogo} id='logoVueling'/>
    </div>
  )
}
