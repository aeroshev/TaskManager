import React from 'react';
import PropTypes from 'prop-types';
import Header from '../Header';
import Footer from '../Footer';

export default function WorkSpace(props) {
  // eslint-disable-next-line no-unused-vars
  const { url } = props;
  return (
    <div>
      <Header />
      <div>
        Hello, from page!
      </div>
      <Footer />
    </div>
  );
}

WorkSpace.propTypes = {
  url: PropTypes.string.isRequired,
};
