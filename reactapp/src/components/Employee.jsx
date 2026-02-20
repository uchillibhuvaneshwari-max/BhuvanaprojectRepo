import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { FaEye, FaEdit, FaTrash } from "react-icons/fa";
import { toast } from "react-toastify";


function Employee() {
  const [employees, setEmployees] = useState([]);


  const fetchEmployees = () => {
    axios
      .get("http://127.0.0.1:8000/api/")
      .then((res) => {
        setEmployees(res.data);
      })
      .catch(() => {
        toast.error("Failed to load employees");
      });
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const deleteEmployee = (id) => {
    if (!window.confirm("Are you sure you want to delete?")) return;

    axios
      .delete(`http://127.0.0.1:8000/api/${id}/`)
      .then(() => {
        toast.success("Employee Deleted Successfully");
        fetchEmployees();
      })
      .catch(() => {
        toast.error("Delete failed");
      });
  };

  return (
    <React.Fragment>
      <div className="container mt-4">
        <h1 className="text-primary text-center">Employee</h1>

        <p>
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Officiis blanditiis quis consequuntur inventore quibusdam, consequatur rem cupiditate distinctio culpa officia ullam tenetur doloremque totam quam obcaecati eos adipisci quisquam voluptatem porro dicta deleniti! Deserunt corrupti architecto illo maxime nostrum odio.
        </p>

        <Link
          to="/add"
          className="btn btn-primary btn-md rounded-pill"
        >
          Add Employee
        </Link>
      </div>

      <div className="container mt-4">
        {employees.length > 0 ? (
          <div className="container">
            <table className="table table-bordered table-striped shadow table-hover">
              <thead className="table-info">
                <tr>
                  <th>ENO</th>
                  <th>ENAME</th>
                  <th>ESAL</th>
                  <th>EADDR</th>
                  <th>ACTIONS</th>
                </tr>
              </thead>

              <tbody>
                {employees.map((emp) => (
                  <tr key={emp.id}>
                    <td>{emp.eno}</td>
                    <td>{emp.ename}</td>
                    <td>{emp.esal}</td>
                    <td>{emp.eaddr}</td>

                    <td>
                      <Link
                        to={`/view/${emp.id}`}
                        className="mr-3 text-primary"
                      >
                        <FaEye size={24} />
                      </Link>

                      <Link
                        to={`/edit/${emp.id}`}
                        className="mr-3 text-success"
                      >
                        <FaEdit size={24} />
                      </Link>

                      <FaTrash
                        size={20}
                        className="text-danger"
                        style={{ cursor: "pointer" }}
                        onClick={() => deleteEmployee(emp.id)}
                      />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <p className="text-center mt-4">No Employees Found</p>
        )}
      </div>
    </React.Fragment>
  );
}

export default Employee;
