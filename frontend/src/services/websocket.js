import { useEffect, useState } from 'react';

const useWebSocket = (url) => {
  const [data, setData] = useState(null);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    const socket = new WebSocket(url);

    socket.onopen = () => setIsOpen(true);
    socket.onclose = () => setIsOpen(false);
    socket.onmessage = (event) => setData(JSON.parse(event.data));

    return () => socket.close();
  }, [url]);

  return { data, isOpen };
};

export default useWebSocket;