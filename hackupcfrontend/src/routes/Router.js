import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import GameStatusPage from '../pages/GameStatusPage';
import LandingPage from '../pages/LandingPage';
import WinnersPage from '../pages/WinnersPage';
import GamePageAnswer from '../pages/GamePageAnswer'
import GamePageDrawer from '../pages/GamePageDrawer';
import LobbysPage from '../pages/LobbysPage';
import SelectionFrase from '../pages/SelectionFrase';

export default function Router() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path='/' element={<LandingPage/>}></Route>
            <Route path='/landing' element={<LandingPage />} ></Route>
            <Route path='/gameDrawer' element={<GamePageDrawer/>}></Route>
            <Route path='/gameAnswer' element={<GamePageAnswer/>}></Route>
            <Route path='/status' element={<GameStatusPage/>}></Route>
            <Route path='/winners' element={<WinnersPage/>}></Route>
            <Route path='/lobbys' element={<LobbysPage/>}></Route>
            <Route path='/selectionFrase' element={<SelectionFrase/>}></Route>
        </Routes>
    </BrowserRouter>
  )
}


