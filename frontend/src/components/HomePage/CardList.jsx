import React from 'react';
import Card from './Card';

export default function CardList() {
  const list = [];
  for (let i = 0; i < 3; i += 1) {
    list.push(<Card />);
  }
  return (
    <div>{list}</div>
  );
}
