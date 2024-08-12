// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import Wave from './components/background/Wave'
import Navigation from './components/navigation/Navigation'

function App() {

  return (
    <>
      <Navigation />
      <Wave/>
      <p>Lidor and Eyal's Habit Tracker Website! Enjoy</p>
      <Wave />
    </>
  );
}

export default App
