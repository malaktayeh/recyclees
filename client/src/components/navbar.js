import React from "react";
import Logo from "../assets/logo_black_md.png";
import Home from "../views/Home"

import { useAuth0 } from "../react-auth0-spa";
import { Navbar, Nav, NavDropdown, Button } from "react-bootstrap";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";


const Navigation = () => {
  const { isAuthenticated, loginWithRedirect, logout } = useAuth0();

  return (
    <Router>
      <Navbar bg="light" expand="lg" fixed="top">
          <Navbar.Brand as={Link} to="/">
            <img
              alt="Home page"
              src={Logo}
              width="30"
              height="30"
              className="d-inline-block align-top"
            />{" "}
            recyclees
          </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="#link">Link</Nav.Link>
            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Another action
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Separated link
              </NavDropdown.Item>
            </NavDropdown>
          </Nav>
            {!isAuthenticated && (
              <Button variant="outline-primary" onClick={() => loginWithRedirect({})}>Log in</Button>
            )}

            {isAuthenticated && (
              <Button variant="outline-primary" onClick={() => logout()}>Log out</Button>
            )}
        </Navbar.Collapse>
      </Navbar>

      <Switch>
         <Route path="/login">
           <Home />
         </Route>
         <Route path="/logout">
           <Home />
         </Route>
         <Route path="/">
           <Home />
         </Route>
       </Switch>
    </Router>
  );
}

export default Navigation;
