import React from 'react';
import './App.css';
import Library from './components/Library';

function Welcome(props: any) {
  return <h1>{props.name} </h1>;
}

function App() {
  return (
    <div className="App">
      <Welcome name='Darlyng'/>
      <Library />
    </div>
  );
}

export default App;
