import React from 'react';
import PropTypes from 'prop-types';
import { useHistory, useLocation } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { useAuth } from '../Auth/Context';

export default function Register(props) {
  // eslint-disable-next-line no-unused-vars
  const { url, handler } = props;
  const history = useHistory();
  const location = useLocation();
  const auth = useAuth();
  const {
    register,
    handleSubmit,
  } = useForm();
  const { from } = location.state || { from: { pathname: '/home/' } };
  const login = () => {
    auth.signin(() => {
      history.replace(from);
    });
  };
  return (
    <form onSubmit={handleSubmit(login)}>
      <input name="email" type="text" placeholder="email" ref={register} />
      <input name="password" type="password" placeholder="password" ref={register} />
      <input name="Submit" type="submit" value="Submit" />
      {/* eslint-disable-next-line react/button-has-type */}
      <button onClick={() => { handler(false); }}>Back</button>
    </form>
  );
}

Register.propTypes = {
  url: PropTypes.string.isRequired,
  handler: PropTypes.func.isRequired,
};
