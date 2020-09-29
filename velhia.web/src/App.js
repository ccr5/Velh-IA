import React from 'react';
import './App.css';
import Header from './structure/Header';
import Footer from './structure/Footer';
import Main from './mainscreen/Main';

function App() {
  const height = window.innerHeight
  return (
    <div className="App">
      <Header />
      <Main height={height} />
      <Footer />
    </div >
  );
}

export default App;
