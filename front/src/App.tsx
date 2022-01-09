import React from 'react';
import './App.css';
import Library from './components/Library';
import NavBar from './components/NavBar';

function Welcome(props: any) {
  return <h1>{props.name} </h1>;
}

function App() {
  return (
    <div className="App">
      <NavBar />
      <Welcome name='Darlyng'/>
      <Library />
    </div>
  );
}

export default App;
