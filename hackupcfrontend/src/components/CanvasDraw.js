import '../css/CanvasDraw.css';
import React, { useRef, useState, useEffect } from "react";
import IP from '../ip';
import axios from 'axios';


export default function CanvasDraw() {
    const [isDrawing, setIsDrawing] = useState(false);
    const [color, setColor] = useState("#3B3B3B");
    const [size, setSize] = useState("3");
    const canvasRef = useRef(null);
    const ctx = useRef(null);
    const [cursor, setCursor] = useState("default");

    const handleSendImage = () => {
      const canvas = canvasRef.current;
      const image = canvas.toDataURL('image/png');
      return image;
    
      // Convierte el contenido del canvas a una imagen en formato de datos de URL
      // Aquí puedes enviar la imagen al servidor o utilizarla en una etiqueta de imagen
    };


    useEffect(()=>{
      let room = localStorage.getItem("roomID");
      setInterval(async ()=>{
        let image = handleSendImage();
        console.log(image);
        let data = new FormData();
        let config = {
          method: 'post',
          maxBodyLength: Infinity,
          url: `http://${IP}:5000/room/${room}/postImg`,
          
          data : data
        };
        data.append('image_data', image);
        let response = axios.request(config).then((response) => {
          console.log(JSON.stringify(response.data));
        })
        .catch((error) => {
          console.log(error);
        });
      },2000);
    },[])
  
    useEffect(() => {
      const canvas = canvasRef.current;
      ctx.current = canvas.getContext("2d");
  
      //Resizing
      canvas.height = 450;
      canvas.width = 650;
  
    }, []);
  
    const startPosition = ({ nativeEvent }) => {
      setIsDrawing(true);
      draw(nativeEvent);
    };
  
    const finishedPosition = () => {
      setIsDrawing(false);
      ctx.current.beginPath();
    };
  
    const draw = ({ nativeEvent }) => {
      if (!isDrawing || !nativeEvent) {
        return;
      }
      
      const canvas = canvasRef.current;
      ctx.current = canvas.getContext("2d");
      ctx.current.lineWidth = size;
      ctx.current.lineCap = "round";
      ctx.current.strokeStyle = color;
  
      const rect = canvas.getBoundingClientRect();
        const x = nativeEvent.clientX - rect.left;
        const y = nativeEvent.clientY - rect.top;

        ctx.current.lineTo(x, y);
        ctx.current.stroke();
        ctx.current.beginPath();
        ctx.current.moveTo(x, y);
    };
  
    const clearCanvas = () => {
      const canvas = canvasRef.current;
      const context = canvas.getContext("2d");
      context.fillStyle = "white";
      context.fillRect(0, 0, canvas.width, canvas.height);
    };
  
    const getPen = () => {
      setCursor("default");
      setSize("3");
      setColor("#3B3B3B");
    };
  
    const eraseCanvas = () => {
      setCursor("grab");
      setSize("20");
      setColor("#FFFFFF");
  
      if (!isDrawing) {
        return;
      }
    };
  
    return (
      <>
        <div className="canvas-btn">
          <button onClick={getPen} className="btn-width">
            Pencil
          </button>
          <div className="btn-width">
            <input
              type="color"
              value={color}
              onChange={(e) => setColor(e.target.value)}
            />
          </div>
          <div>
            <select
              className="btn-width"
              value={size}
              onChange={(e) => setSize(e.target.value)}
            >
              <option> 1 </option>
              <option> 3 </option>
              <option> 5 </option>
              <option> 10 </option>
              <option> 15 </option>
              <option> 20 </option>
              <option> 25 </option>
              <option> 30 </option>
            </select>
          </div>
          <button onClick={clearCanvas} className="btn-width">
            Clear
          </button>
          <div>
            <button onClick={eraseCanvas} className="btn-width">
              Eras
            </button>
          </div>
        </div>
      <canvas
       style={{ cursor: cursor }}
        onMouseDown={startPosition}
        onMouseUp={finishedPosition}
        onMouseMove={draw}
        ref={canvasRef}
      />
    </>
  );
}
