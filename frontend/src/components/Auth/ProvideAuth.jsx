import React from 'react';
import PropTypes from 'prop-types';
import { authContext, useProvideAuth } from './Context';

export default function ProvideAuth({ children }) {
  const auth = useProvideAuth();
  return (
    <authContext.Provider value={auth}>
      {children}
    </authContext.Provider>
  );
}

ProvideAuth.propTypes = {
  children: PropTypes.element.isRequired,
};
