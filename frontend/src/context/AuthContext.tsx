import React, { createContext, useContext } from "react";
import { AuthServiceProps } from "../@types/auth-service";
import { useAuthService } from "../services/AuthServices.ts";

/**
 * Context for authentication services.
 * Provides the AuthServiceProps interface for accessing authentication methods and state.
 */
const AuthServiceContext = createContext<AuthServiceProps | null>(null);

/**
 * AuthServiceProvider component.
 * Wraps around parts of the app that need access to authentication services.
 *
 * @param {React.PropsWithChildren<{}>} props - The props, including children, passed to the provider.
 * @returns {JSX.Element} The provider component that supplies authentication services.
 */
export function AuthServiceProvider(props: React.PropsWithChildren<{}>): JSX.Element {
  // Using the custom hook to get authentication services
  const authServices = useAuthService();

  return (
    <AuthServiceContext.Provider value={authServices}>
      {props.children}
    </AuthServiceContext.Provider>
  );
}

/**
 * Custom hook to use the AuthServiceContext.
 * 
 * @returns {AuthServiceProps} The authentication service properties and methods.
 * @throws {Error} If the hook is used outside of the AuthServiceProvider.
 */
export function useAuthServiceContext(): AuthServiceProps {
  const context = useContext(AuthServiceContext);

  // Throw an error if the hook is used outside of the AuthServiceProvider
  if (context === null) {
    throw new Error("Error - You have to use the AuthServiceProvider");
  }

  return context;
}

export default AuthServiceProvider;
