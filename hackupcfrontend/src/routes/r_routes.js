import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


export default function r_routes() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path='/' element={<p_landingPage/>}></Route>
            <Route path='/landing' element={<p_landingPage/>}></Route>
        </Routes>
    </BrowserRouter>
  )
}


