import React, { useState } from 'react';
import axios from 'axios';

const BotControl = () => {
  const [isRunning, setIsRunning] = useState(false);

  const toggleBot = async () => {
    const action = isRunning ? 'stop' : 'start';
    try {
      await axios.post(`/api/bot/${action}`);
      setIsRunning(!isRunning);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <button onClick={toggleBot}>
        {isRunning ? 'Stop Bot' : 'Start Bot'}
      </button>
    </div>
  );
};

export default BotControl;