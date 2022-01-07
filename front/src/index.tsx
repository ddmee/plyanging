import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Clock from './Clock';
import Library from './Library';
import reportWebVitals from './reportWebVitals';


function Welcome(props: any) {
  return <h1>{props.name} </h1>;
}


ReactDOM.render(
  <React.StrictMode>
    <Welcome name='Darlyng' />
    <Library />
  </React.StrictMode>,
  document.getElementById('root')
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
