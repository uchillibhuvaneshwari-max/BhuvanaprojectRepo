import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link, useNavigate, useParams } from "react-router-dom";
import { toast } from "react-toastify";

const API_URL = "http://127.0.0.1:8000/api/";

export default function EditEmployee() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [emp, setEmp] = useState({
    eno: "",
    ename: "",
    esal: "",
    eaddr: "",
  });




  useEffect(() => {
    axios
      .get(`${"http://127.0.0.1:8000/api/"}${id}/`)
      .then((res) => {
        setEmp(res.data);
        setLoading(false);
      })
      .catch(() => {
        toast.error("Failed to load employee");
        setLoading(false);
      });
  }, [id]);


  const handleChange = (e) => {
    setEmp({ ...emp, [e.target.name]: e.target.value });
  };

 
  const updateEmployee = () => {
    axios
      .put(`${"http://127.0.0.1:8000/api/"}${id}/`, emp)
      .then(() => {
        toast.success("Employee Updated Successfully");
        navigate("/");
      })
      .catch((err) => {
        console.error(err.response);
        toast.error("Update failed");
      });
  };

  

  return (
    <div className="container mt-5">
      <div className="col-md-5">
        <div className="card shadow">
          <div className="card-header bg-warning text-white text-center">
            <h4>Edit Employee</h4>
          </div>

          <div className="card-body">
            <input
              type="text"
              name="eno"
              className="form-control mb-3"
              value={emp.eno}
              onChange={handleChange}
            />

            <input
              type="text"
              name="ename"
              className="form-control mb-3"
              value={emp.ename}
              onChange={handleChange}
            />

            <input
              type="number"
              name="esal"
              className="form-control mb-3"
              value={emp.esal}
              onChange={handleChange}
            />

            <input
              type="text"
              name="eaddr"
              className="form-control mb-3"
              value={emp.eaddr}
              onChange={handleChange}
            />
            <Link
              onClick={updateEmployee}
              className="btn btn-success rounded-pill me-2"
            >
              UPDATE
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
