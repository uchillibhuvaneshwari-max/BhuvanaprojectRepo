import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams, Link } from "react-router-dom";
import { toast } from "react-toastify";


export default function ViewEmployee() {
  const { id } = useParams();
  const [emp, setEmp] = useState(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/${id}/`)
      .then((res) => {
        setEmp(res.data);
      })
      .catch((err) => {
        console.error(err);
        toast.error("Failed to load employee");
      });
  }, [id]);

  if (!emp) {
    return <p className="text-center mt-5">Loading...</p>;
  }
  
  return (
    <div className="container mt-5">
      <div className="col-md-5 mx-auto">
        <div className="card shadow">
          <div className="card-header bg-info text-white text-center">
            <h4>View Employee</h4>
          </div>

          <div className="card-body">
            <p>Employee No:{emp.eno}</p>
            <p>Name: {emp.ename}</p>
            <p>Salary: {emp.esal}</p>
            <p>Address: {emp.eaddr}</p>

            <Link to="/" className="btn btn-warning btn-outline-amber">
              BACK
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
