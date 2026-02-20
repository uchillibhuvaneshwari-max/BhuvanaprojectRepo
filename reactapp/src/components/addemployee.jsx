import React, { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

const API_URL = "http://127.0.0.1:8000/api/";

export default function AddEmployee() {
  const navigate = useNavigate();

  const [emp, setEmp] = useState({
    eno: "",
    ename: "",
    esal: "",
    eaddr: "",
  });

  const handleChange = (e) => {
    setEmp({ ...emp, [e.target.name]: e.target.value });
  };

  const saveEmployee = () => {
    axios
      .post("http://127.0.0.1:8000/api/", emp)
      .then(() => {
        toast.success("Employee Added Successfully");
        navigate("/");
      })
      .catch((err) => {
        console.error(err.response);
        toast.error("Failed to add employee");
      });
  };

  return (
    <div className="container mt-5">
      <div className="col-md-5">
        <div className="card shadow">
          <div className="card-header bg-primary text-white text-center">
            <h4>Add Employee</h4>
          </div>

          <div className="card-body">
            <input
              type="text"
              name="eno"
              placeholder="Employee No"
              className="form-control mb-3"
              value={emp.eno}
              onChange={handleChange}
            />

            <input
              type="text"
              name="ename"
              placeholder="Employee Name"
              className="form-control mb-3"
              value={emp.ename}
              onChange={handleChange}
            />

            <input
              type="number"
              name="esal"
              placeholder="Salary"
              className="form-control mb-3"
              value={emp.esal}
              onChange={handleChange}
            />

            <input
              type="text"
              name="eaddr"
              placeholder="Address"
              className="form-control mb-3"
              value={emp.eaddr}
              onChange={handleChange}
            />
            <Link
              onClick={saveEmployee}
              className="btn btn-success rounded-pill me-2"
            >
              ADD
            </Link>

            <Link to="/" className="btn btn-secondary rounded-pill">
              BACK
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
