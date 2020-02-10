import React, { Fragment } from "react";
import { Container } from "react-bootstrap";

import Hero from "../components/homehero";
// import Content from "../components/Content";

const Home = () => (
  <Fragment>
    <Hero />
    <Container >
      {/* <Content /> */}
    </Container>
  </Fragment>
);

export default Home;
