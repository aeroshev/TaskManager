import React from 'react';
import { Card } from './Card'

export function CardList() {
    const list = [];

    for (let i = 0; i < 3; i++) {
        list.push(<Card/>)
    }
    return (
        <div>{list}</div>
    )
}
