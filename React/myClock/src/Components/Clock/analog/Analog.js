import React from 'react'
import './Analog.css'

class Analog extends React.Component{
  state={
      time: Date().toLocaleString(),
      hours: new Date().toLocaleTimeString(),
      minutes: new Date().toLocaleTimeString(),
      seconds: new Date().toLocaleTimeString(),
  }
  componentDidMount(){
    this.intervalID = setInterval(
        ()=> this.getHour(), 1000 
    )
    this.intervalID = setInterval(
        ()=> this.getMinutes(), 1000 
    )
    this.intervalID = setInterval(
        ()=> this.getSecond(), 1000 
    )
    }
    componentWillUnmount(){
        clearInterval(this.intervalID)
    } 
  getHour (){
    this.setState({
        hours: new Date().getHours()
    })
}
getMinutes (){
      
    this.setState({
        minutes: new Date().getMinutes()
    })
}
getSecond (){
      
    this.setState({
        seconds: new Date().getSeconds()
    })
}

render(){
        return(
            <>
                <div id='clockHead'>
                    <div id='hours' className='hands'>
                        {this.state.hours}
                    </div>
                    <div id='seconds' className='hands'>
                        {this.state.seconds}
                    </div>
                    <div id='minutes' className='hands'>
                        {this.state.minutes}
                    </div>
                </div>
            </>
        )
    }
}

export default Analog