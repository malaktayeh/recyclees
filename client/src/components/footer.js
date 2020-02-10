import React from "react";
import logo from "../assets/logo.svg";

const Footer = () => (
  <footer className="bg-light p-3 text-center">
    <a href="/">
      <img className="mb-3 app-logo" src={logo} alt="recyclees logo" width="40" />
    </a>
    <p>&copy; Copyright 2020, recyclees</p>
  </footer>
);

export default Footer;
