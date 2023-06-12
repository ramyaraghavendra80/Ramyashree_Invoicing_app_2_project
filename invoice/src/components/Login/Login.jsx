import "./Login.css";
import { Formik, ErrorMessage, Field, Form } from "formik";
import * as Yup from "yup";
import Button from "react-bootstrap/esm/Button";
import Navbar from "../NavBar/Navbar";
import { Link, useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();
  const initialValues = {
    email_id: "",
    password: "",
  };
  const submitForm = (values) => {
    console.log(values);
    fetch("http://127.0.0.1:8000/project/user/signin/", {
      method: "POST",
      body: JSON.stringify(values),
      headers: {
        "Content-Type": "application/json",
      },
    }).then((res) => res.json()).then((data)=>{
        if(data.state){
            localStorage.setItem("token",data.token)
            navigate("/")
        }
        else{
            alert(data.message)
        }
    });
  };
  const LoginSchema = Yup.object().shape({
    email_id: Yup.string()
      .email("Email format is invalid")
      .required("Email is required"),
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
                      type="email"
                      name="email_id"
                      id="email"
                      placeholder="Enter email"
                      className={`inputfield ${
                        errors.email && touched.email ? "input-error" : null
                      }`}
                    />
                    <ErrorMessage
                      name="email_id"
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
