import React, { useEffect, useState } from 'react'
import axios from 'axios';
import Lobby from '../components/Lobby';
import '../css/LobbysPage.css';
import { useNavigate  } from 'react-router-dom';

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
                let response = await axios.post("http://192.168.137.220:5000/connect", {
                    username: username,
                    room: '0'
                });
                if (response.data.succes){
                    navigation("/landing");
                }
            } catch (error){
                alert("NEIN");
            }
        }
    }

    useEffect(() =>{
        let getLobbys = async () =>{
            try{
                let response = await axios.get("http://192.168.137.220:5000/rooms");
                if (response) {
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


    const handleClick = async (e, lobbyID, numPlayers) => {
        if (numPlayers != 8 && username != "" && username !== "Write your username"){
            try {
                let response = await axios.post("http://192.168.137.220:5000/connect", {
                    username: username,
                    room: lobbyID
                });
                if (response.data.succes){
                    navigation("/landing");
                }
            } catch (error){
                alert("NEIN");
            }
        }
    }

  return (
    <div className='lobbysPage'>
        <input placeholder={username} onChange={(e) => handleUser(e)} className='inputName'></input>
        <div className='lobbysList'>
        {
            lobbys.map((lobby) => (
                <Lobby key={lobby.id} name={lobby.id} numPlayers={lobby.numPlayers} onClick={(e) => handleClick()} />
            ))
        }
        </div>
        {
            lobbys.length == 0 && (
                <>
                    <button onClick={(e) => handleCreateRoom(e)}>Create Room</button>
                </>
            )
        }
    </div>
  )
}
