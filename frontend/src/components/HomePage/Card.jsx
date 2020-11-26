import React from 'react';
import { Link } from 'react-router-dom';

export default function Card() {
  return (
    <div>
      <Link to="/content/">
        Card!
      </Link>
    </div>
  );
}
