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
 * Login component that handles user login functionality.
 *
 * @returns {JSX.Element} The Login component.
 */
const Login = (): JSX.Element => {
  const { login } = useAuthServiceContext();
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
      const status = await login(username, password);
      if (status === 401) {
        console.log("Unauthorised");
        formik.setErrors({
          username: "Invalid username or password",
          password: "Invalid username or password",
        });
      } else {
        navigate("/");
      }
    },
  });

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          alignItems: "center",
          flexDirection: "column",
        }}
      >
        <Typography
          variant="h5"
          noWrap
          component="h1"
          sx={{
            fontWeight: 500,
            pb: 2,
          }}
        >
          Sign in
        </Typography>
        <Box component="form" onSubmit={formik.handleSubmit} sx={{ mt: 1 }}>
          <TextField
            autoFocus
            fullWidth
            id="username"
            name="username"
            label="username"
            value={formik.values.username}
            onChange={formik.handleChange}
            error={!!formik.touched.username && !!formik.errors.username}
            helperText={formik.touched.username && formik.errors.username}
          ></TextField>
          <TextField
            margin="normal"
            fullWidth
            id="password"
            name="password"
            type="password"
            label="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            error={!!formik.touched.password && !!formik.errors.password}
            helperText={formik.touched.password && formik.errors.password}
          ></TextField>
          <Button
            variant="contained"
            disableElevation
            type="submit"
            sx={{ mt: 1, mb: 2 }}
          >
            Next
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default Login;
