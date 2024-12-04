import axios from 'axios';
import { AuthServiceProps } from '../@types/auth-service';
import { useState } from 'react';
import { BASE_URL } from '../config.ts';
import { useNavigate } from 'react-router-dom';

/**
 * Custom hook to provide authentication services.
 *
 * @returns {AuthServiceProps} The authentication service properties and methods.
 */
export function useAuthService(): AuthServiceProps {
  const navigate = useNavigate();

  /**
   * Gets the initial logged-in value from localStorage.
   *
   * @returns {boolean} The initial logged-in status.
   */
  const getInitialLoggedInValue = () => {
    const loggedIn = localStorage.getItem('isLoggedIn');
    return loggedIn !== null && loggedIn === 'true';
  };

  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(getInitialLoggedInValue);

  /**
   * Fetches user details from the server.
   */
  const getUserDetails = async () => {
    try {
      const userId = localStorage.getItem('user_id');
      const response = await axios.get(`http://127.0.0.1:8000/api/users/?user_id=${userId}`, {
        withCredentials: true,
      });
      const userDetails = response.data;
      localStorage.setItem('username', userDetails.username);
      setIsLoggedIn(true);
      localStorage.setItem('isLoggedIn', 'true');
    } catch (err: any) {
      setIsLoggedIn(false);
      localStorage.setItem('isLoggedIn', 'false');
      return err;
    }
  };

  /**
   * Logs in the user with the provided username and password.
   *
   * @param {string} username - The username of the user.
   * @param {string} password - The password of the user.
   * @returns {Promise<number | undefined>} The status code or undefined if successful.
   */
  const login = async (username: string, password: string) => {
    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/token/',
        {
          username,
          password,
        },
        { withCredentials: true }
      );

      const user_id = response.data.user_id;
      localStorage.setItem('isLoggedIn', 'true');
      localStorage.setItem('user_id', user_id);
      setIsLoggedIn(true);
      getUserDetails();
    } catch (err: any) {
      return err.response.status;
    }
  };

  /**
   * Refreshes the user's access token.
   */
  const refreshAccessToken = async () => {
    try {
      await axios.post(`${BASE_URL}/token/refresh/`, {}, { withCredentials: true });
    } catch (refreshError) {
      return Promise.reject(refreshError);
    }
  };

  /**
   * Registers a new user with the provided username and password.
   *
   * @param {string} username - The desired username for the new user.
   * @param {string} password - The desired password for the new user.
   * @returns {Promise<number>} The status code of the registration response.
   */
  const register = async (username: string, password: string) => {
    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/register/',
        {
          username,
          password,
        },
        { withCredentials: true }
      );
      return response.status;
    } catch (err: any) {
      return err.response.status;
    }
  };

  /**
   * Logs out the current user.
   */
  const logout = async () => {
    localStorage.setItem('isLoggedIn', 'false');
    localStorage.removeItem('user_id');
    localStorage.removeItem('username');
    setIsLoggedIn(false);
    navigate('/login');

    try {
      await axios.post(`${BASE_URL}/logout/`, {}, { withCredentials: true });
    } catch (refreshError) {
      return Promise.reject(refreshError);
    }
  };

  return { login, isLoggedIn, logout, refreshAccessToken, register };
}
