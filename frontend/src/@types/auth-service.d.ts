export interface AuthServiceProps {
  /**
   * Method to log in a user with a username and password.
   * @param username - The username of the user.
   * @param password - The password of the user.
   * @returns Any type, which could be an authentication token, user details, etc.
   */
  login: (username: string, password: string) => any;

  /**
   * Boolean value indicating whether the user is currently logged in.
   */
  isLoggedIn: boolean;

  /**
   * Method to log out the current user.
   */
  logout: () => void;

  /**
   * Method to refresh the current user's access token.
   * @returns A promise that resolves once the token has been refreshed.
   */
  refreshAccessToken: () => Promise<void>;

  /**
   * Method to register a new user with a username and password.
   * @param username - The desired username for the new user.
   * @param password - The desired password for the new user.
   * @returns A promise that resolves with any type, which could include user details, a confirmation message, etc.
   */
  register: (username: string, password: string) => Promise<any>;
}
