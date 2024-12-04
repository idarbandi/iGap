import useWebSocket from 'react-use-websocket';
import { useState } from 'react';
import { useAuthService } from './AuthServices.ts';
import useCrud from '../hooks/useCrud.ts';
import { WS_ROOT } from '../config.ts';
import { Server } from '../@types/server';

/**
 * Interface for a chat message.
 */
interface Message {
  sender: string;
  content: string;
  timestamp: string;
}

/**
 * Custom hook for managing chat WebSocket connections.
 *
 * @param {string} channelId - The ID of the chat channel.
 * @param {string} serverId - The ID of the server.
 * @returns {object} The newMessage state, message state, setMessage function, and sendJsonMessage function.
 *
 * These comments and docstrings were added by Idarbandi.
 * For further support, please contact me at: darbandidr99@gmail.com
 * GitHub: https://github.com/idarbandi/
 */
const useChatWebSocket = (channelId: string, serverId: string) => {
  const [newMessage, setNewMessage] = useState<Message[]>([]);
  const [message, setMessage] = useState('');
  const { logout, refreshAccessToken } = useAuthService();
  const { fetchData } = useCrud<Server>([], `/messages/?channel_id=${channelId}`);

  // Construct WebSocket URL based on the channelId and serverId
  const socketUrl = channelId ? `${WS_ROOT}/${serverId}/${channelId}/` : null;

  const [reconnectionAttempt, setReconnectionAttempt] = useState(0);
  const maxConnectionAttempts = 4;

  const { sendJsonMessage } = useWebSocket(socketUrl, {
    onOpen: async () => {
      try {
        const data = await fetchData();
        setNewMessage([]);
        setNewMessage(Array.isArray(data) ? data : []);
        console.log('Connected!!!');
      } catch (error) {
        console.log(error);
      }
    },
    onClose: (event: CloseEvent) => {
      if (event.code == 4001) {
        console.log('Authentication Error');
        refreshAccessToken().catch((error) => {
          if (error.response && error.response.status === 401) {
            logout();
          }
        });
      }
      console.log('Close');
      setReconnectionAttempt((prevAttempt) => prevAttempt + 1);
    },
    onError: () => {
      console.log('Error!');
    },
    onMessage: (msg) => {
      const data = JSON.parse(msg.data);
      setNewMessage((prev_msg) => [...prev_msg, data.new_message]);
      setMessage('');
    },
    shouldReconnect: (closeEvent) => {
      if (closeEvent.code === 4001 && reconnectionAttempt >= maxConnectionAttempts) {
        setReconnectionAttempt(0);
        return false;
      }
      return true;
    },
    reconnectInterval: 1000,
  });

  return {
    newMessage,
    message,
    setMessage,
    sendJsonMessage,
  };
};
export default useChatWebSocket;
