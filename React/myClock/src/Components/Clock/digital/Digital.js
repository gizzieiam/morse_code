import React, { Component } from 'react'
import './Digital.css'
// let time = new Date().toLocaleTimeString()
// console.log(time);

class Digital extends React.Component{
    state ={
        time: Date().toLocaleString(),
        date: new Date().toLocaleDateString(),
        active: false,
        changeActive:{},
    }
    
    componentDidMount(){
        this.intervalID = setInterval(
            ()=> this.check(), 1000
            )
        }
        componentWillUnmount(){
            clearInterval(this.intervalID)
        }
        check(){
            this.setState({
                time: new Date().toLocaleTimeString()
            })
    }
        
        digitalBtn = ()=>{
            let changeBtn = document.getElementById('Digbtn')
            changeBtn.style.display='none'

            let changeBtn2 = document.getElementById('Digbtn2')
            changeBtn2.style.display='inline'
            let time = document.getElementById('digTime')
            time.style.display='inline'
      
       
        }
        showAgain = ()=>{
            let changeBtn3 = document.getElementById('Digbtn')
            changeBtn3.style.display='inline'

            let changeBtn4 = document.getElementById('Digbtn2')
            changeBtn4.style.display='none'

            let time2 = document.getElementById('digTime')
            time2.style.display='none'
        }

        
        render(){
            return(
                <>
                <button id='Digbtn' className='btn' onClick={this.digitalBtn}>Digial Clock</button>
                <button id='Digbtn2' className='btn' onClick={this.showAgain}>Hide Clock</button>
                <p id='digTime'>{this.state.time}</p>
            </>
        )
    }
}

export default Digital