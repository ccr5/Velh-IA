import React from 'react';
import './App.css';
import Header from './structure/Header';
import Footer from './structure/Footer';
import Content from './structure/Content';

function App() {
  return (
    <div className="App">
      <Header />
      <Content />
      <Footer />
    </div>
  );
}

export default App;
