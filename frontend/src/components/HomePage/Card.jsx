import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

export default function Card(props) {
  // eslint-disable-next-line no-unused-vars
  const { content } = props;
  return (
    <div>
      <Link to="/content/">
        Card!
      </Link>
    </div>
  );
}

Card.defaultProps = {
  content: {},
};

Card.propTypes = {
  content: PropTypes.objectOf(PropTypes.string),
};
