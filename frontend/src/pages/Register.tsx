/**
 * These comments and docstrings were added by Idarbandi.
 * For further support, please contact me at: darbandidr99@gmail.com
 * GitHub: https://github.com/idarbandi/
 */

import { useFormik } from "formik";
import { useNavigate } from "react-router-dom";
import { useAuthServiceContext } from "../context/AuthContext.tsx";
import { Box, Button, Container, TextField, Typography } from "@mui/material";

/**
 * Register component that handles user registration functionality.
 *
 * @returns {JSX.Element} The Register component.
 */
const Register = (): JSX.Element => {
  const { register } = useAuthServiceContext();
  const navigate = useNavigate();
  
  const formik = useFormik({
    initialValues: {
      username: "",
      password: "",
    },
    validate: (values) => {
      const errors: Partial<typeof values> = {};
      if (!values.username) {
        errors.username = "Required";
      }
      if (!values.password) {
        errors.password = "Required";
      }
      return errors;
    },
    onSubmit: async (values) => {
      const { username, password } = values;
      const status = await register(username, password);
      if (status === 409) {
        formik.setErrors({
          username: "Invalid username",
        });
      } else if (status === 401) {
        console.log("Unauthorised");
        formik.setErrors({
          username: "Invalid username or password",
          password: "Invalid username or password",
        });
      } else {
        navigate("/login");
      }
    },
  });

