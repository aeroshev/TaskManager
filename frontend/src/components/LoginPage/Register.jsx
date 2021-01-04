import React from 'react';
import PropTypes from 'prop-types';
import { useForm } from 'react-hook-form';
import styles from '../../styles/Register.module.css';

export default function Register(props) {
  // eslint-disable-next-line no-unused-vars
  const { url } = props;
  const {
    register,
    handleSubmit,
  } = useForm();
  return (
    <div>Empty</div>
  );
}

Register.propTypes = {
  url: PropTypes.string.isRequired,
};
