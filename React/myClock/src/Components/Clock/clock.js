import React, { Component } from 'react'
import './clock.css'
import Digital from './digital/Digital'
import Analog from './analog/Analog'
import Test from './test'

class Clock extends React.Component{

        render(){
            return(
                <>
            <div id='showDigital'>
                <Digital />
            </div>
            <div id='showAnalog'>
                {/* <Analog /> */}
                <Test />
            </div>
            </>
        )
    }
}
export default Clock
