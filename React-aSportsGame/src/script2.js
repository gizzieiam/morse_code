class App extends React.Component{
    render(){
        return (
            console.log('test 1');
            <Team name="Lucky Charms" logo='/src/img/lc.png'/>
        )
    }
}
ReactDOM.render(<App />, document.getElementById('root')) 