import React, { Fragment } from "react";
import { Container } from "react-bootstrap";

import Hero from "../components/homeHero";
import Content from "../components/homeContent";

const Home = () => (
  <Fragment>
    <Hero />
    <Container >
      <Content />
    </Container>
  </Fragment>
);

export default Home;
