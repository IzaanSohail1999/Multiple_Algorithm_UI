import React, { Component } from 'react'

const Hello = () => {
//         return (
//         <div className='DummyClass'>
//            <h1>Hello Izaan Sohail</h1>
//         </div>
// )

return React.createElement(
    'div',
    {id: 'hello', className: 'DummyClass'},
    React.createElement(
        'h1',
        null,
        'Hello Izaan Boy'
    )
    )

}

export default Hello