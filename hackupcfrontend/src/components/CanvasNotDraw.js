import React, { useRef, useEffect, useState } from 'react';
import axios from 'axios';
import IP from '../ip';

function CanvasComponent () {
  let room = localStorage.getItem("roomID");
  const time = new Date().getTime()

  return (
    <>
      <img src={`http://${IP}:5000/room/${room}/getImg?${time}`} alt="example image" style={{zIndex:1000}} />
    </>
  );
}

export default CanvasComponent;


