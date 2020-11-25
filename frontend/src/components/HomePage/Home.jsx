import React from 'react';
import { HeaderHome } from './HeaderHome'
import { CardList } from './CardList';


export function Home() {
    return (
        <div>
            <HeaderHome/>
            <div>
                Hello, world!
            </div>
            <CardList/>
        </div>
    );
}