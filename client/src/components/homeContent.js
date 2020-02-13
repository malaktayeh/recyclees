import React, { Fragment } from "react";

import { Row, Col } from "react-bootstrap";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLink } from '@fortawesome/free-solid-svg-icons'

import contentData from "../utils/contentData";

function HomeContent() {
    return (
      <Fragment>
        <h2 className="my-5 text-center">Why donate?</h2>
        <Row className="justify-content-between">
          {contentData.map((col, i) => (
            <Col key={i} md={5} className="mb-4">
              <h6 className="mb-3">
                  <FontAwesomeIcon icon={faLink} className="mr-2" />
                  {col.title}
              </h6>
              <p>{col.description}</p>
            </Col>
          ))}
        </Row>
      </Fragment>
    );
}

export default HomeContent;
