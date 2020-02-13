import React, { useState, useEffect } from "react";
// import Logo from "../assets/logo_black_md.png";
// import Home from '../views/Home';

import { useAuth0 } from "../react-auth0-spa";
// import { Navbar, Nav, NavDropdown, Button } from "react-bootstrap";
// import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const Navigation = () => {
  const { isAuthenticated, loginWithRedirect, logout } = useAuth0();
  // const [buttonClicked, setButtonClicked] = useState(false);

  // useEffect(() => {
  //   if (buttonClicked) {
  //     // do something meaningful, Promises, if/else, whatever, and then
  //     window.location.assign('http://recyclees.auth0.com');
  //   }
  // });

  return (
    <div>
      {!isAuthenticated && (
        <button onClick={() => loginWithRedirect({})}>Log in</button>
      )}

      {isAuthenticated && <button onClick={() => logout()}>Log out</button>}
    </div>
    // <Router>
    //   <Navbar bg="light" expand="lg" fixed="top">
    //       <Navbar.Brand as={Link} to="/">
    //         <img
    //           alt="Home page"
    //           src={Logo}
    //           width="30"
    //           height="30"
    //           className="d-inline-block align-top"
    //         />{" "}
    //         recyclees
    //       </Navbar.Brand>
    //     <Navbar.Toggle aria-controls="basic-navbar-nav" />
    //     <Navbar.Collapse id="basic-navbar-nav">
    //       <Nav className="mr-auto">
    //         <Nav.Link href="#link">Link</Nav.Link>
    //         <NavDropdown title="Dropdown" id="basic-nav-dropdown">
    //           <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
    //           <NavDropdown.Item href="#action/3.2">
    //             Another action
    //           </NavDropdown.Item>
    //           <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
    //           <NavDropdown.Divider />
    //           <NavDropdown.Item href="#action/3.4">
    //             Separated link
    //           </NavDropdown.Item>
    //         </NavDropdown>
    //       </Nav>
    //       <Button 
    //         variant="outline-primary"
    //         onClick={() => {setButtonClicked(true)}}
    //       >
    //         Sign in
    //       </Button>
    //     </Navbar.Collapse>
    //   </Navbar>

    //   <Switch>
    //     <Route path="/login">
    //       <Home />
    //     </Route>
    //     <Route path="/logout">
    //       <Home />
    //     </Route>
    //     <Route path="/">
    //       <Home />
    //     </Route>
    //   </Switch>
    // </Router>
  );
}

export default Navigation;
