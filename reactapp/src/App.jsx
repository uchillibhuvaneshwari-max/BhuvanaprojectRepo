import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Employee from "./components/Employee";
import AddEmployee from "./components/addemployee";
import EditEmployee from "./components/editemployee";
import ViewEmployee from "./components/viewemployee";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  return (
    <Router>
      <ToastContainer position="top-right" autoClose={2000} />

      <Routes>
        <Route path="/" element={<Employee />} />
        <Route path="/add" element={<AddEmployee />} />
        <Route path="/view/:id" element={<ViewEmployee />} />
        <Route path="/edit/:id" element={<EditEmployee />} />
      </Routes>
    </Router>
  );
}

export default App;
