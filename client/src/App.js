import React from 'react';
import Home from './views/Home'
import Navbar from './components/navbar'
import Footer from './components/footer'
import { useAuth0 } from "./react-auth0-spa";

function App() {
  const { loading } = useAuth0();

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="App">
      <header>
        <Navbar />
        <Home />
        <Footer />
      </header>
    </div>
  );
}

export default App;
