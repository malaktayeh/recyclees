import React from 'react';
import { Navbar, Nav, NavDropdown, Button } from 'react-bootstrap';

function Navigation() {
    return(
        <Navbar bg="light" expand="lg">
        <Navbar.Brand href="#home">Recyclees</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
            <Nav.Link href="#link">Link</Nav.Link>
            <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
            </NavDropdown>
            </Nav>
            <Button variant="outline-success">Login!</Button>
        </Navbar.Collapse>
        </Navbar>
    )
}

export default Navigation;
