import React from 'react';
import clock from './clock.png';
import './Clock.css';

const user = {
  firstName: 'Donal',
  lastName: 'Mee'
}


function Clock() {
  return (
    <div className="Clock">
      <header className="Clock-header">
        <img src={clock} className="Clock-image" alt="logo" />
        <h1>Time is Running</h1>
        <p>
          It is {new Date().toLocaleTimeString()}
        </p>
        <p>The time is brought to you by {user.firstName} {user.lastName}</p>
      </header>
    </div>
  );
}

export default Clock;
