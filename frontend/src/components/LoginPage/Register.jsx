import React from 'react';
import PropTypes from 'prop-types';
import { useForm } from 'react-hook-form';

export default function Register(props) {
  // eslint-disable-next-line no-unused-vars
  const { url } = props;
  const {
    register,
    handleSubmit,
  } = useForm();

  const mockFunction = () => {};
  return (
    <form onSubmit={handleSubmit(mockFunction)}>
      <input name="email" type="text" placeholder="email" ref={register} />
      <input name="password" type="password" placeholder="password" ref={register} />
      <input name="Submit" type="submit" value="Submit" />
    </form>
  );
}

Register.propTypes = {
  url: PropTypes.string.isRequired,
};
