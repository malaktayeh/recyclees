import React from 'react';
import Home from './views/Home'
import Navbar from './components/navbar'
import Footer from './components/footer'

function App() {
  return (
    <div className="App">
      <Navbar />
      <Home />
      <Footer />
    </div>
  );
}

export default App;
