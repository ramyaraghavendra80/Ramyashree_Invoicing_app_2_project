import "./Login.css";
import { Formik, ErrorMessage, Field, Form } from "formik";
import * as Yup from "yup";
import Button from "react-bootstrap/esm/Button";
import Navbar from "../NavBar/Navbar";
import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";

function Login() {
  const navigate = useNavigate();
  const initialValues = {
    username: "",
    password: "",
  };

const [username,setUsername]=useState('');
const [password,setPassword]=useState('');

  const submitForm = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/project/user/login/", {
        method: "POST",
        body: JSON.stringify({username,password}),
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (res.ok) {
        throw new Error("Login failed");
      }
      const data = await res.json();
      localStorage.setItem("access", data.access);
      navigate("/");
    } catch (error) {
      console.error("Login unsuccesfull...!", error);
    }
  };
  const LoginSchema = Yup.object().shape({
    username: Yup.string().required("username is required"),
    password: Yup.string().required("Password is required"),
    // .min(6, "Password is too short - should be 6 chars minimum"),
  });

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={LoginSchema}
      onSubmit={submitForm}
    >
      {(formik) => {
        const { errors, touched } = formik;
        return (
          <>
            <Navbar />
            <div className="logincontainer">
              <Form className="loginform">
                <p className="loginheading">Login</p>
                <hr />
                <div className="loginbody">
                  <div className="form-row">
                    <Field
                      type="username"
                      name="username"
                      id="username"
                      placeholder="Enter username"
                      className={`inputfield ${
                        errors.username && touched.username
                          ? "input-error"
                          : null
                      }`}
                    />
                    <ErrorMessage
                      name="username"
                      className="errormsg"
                      component="div"
                    />
                  </div>

                  <div className="form-row">
                    <Field
                      type="password"
                      name="password"
                      id="password"
                      placeholder="Enter password"
                      className={`inputfield ${
                        errors.password && touched.password
                          ? "input-error"
                          : null
                      }`}
                    />
                    <ErrorMessage
                      component="div"
                      className="errormsg"
                      name="password"
                    />
                  </div>
                  <div>
                    <p className="text">
                      Don't have an account?
                      <span>
                        <Link to="/signup" className="signuplink">
                          Signup here
                        </Link>
                      </span>
                    </p>
                  </div>

                  <Button type="submit" className="loginsubmit">
                    Login
                  </Button>
                </div>
              </Form>
            </div>
          </>
        );
      }}
    </Formik>
  );
}

export default Login;
