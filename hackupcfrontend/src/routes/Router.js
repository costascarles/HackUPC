import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import GameStatusPage from '../pages/GameStatusPage';
import LandingPage from '../pages/LandingPage';
import WinnersPage from '../pages/WinnersPage';

export default function Router() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path='/' element={<LandingPage/>}></Route>
            <Route path='/landing' element={<LandingPage/>}></Route>
            <Route path='/status' element={<GameStatusPage/>}></Route>
            <Route path='/winners' element={<WinnersPage/>}></Route>
        </Routes>
    </BrowserRouter>
  )
}


