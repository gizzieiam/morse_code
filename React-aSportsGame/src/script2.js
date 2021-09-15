class App extends React.Component{
    render(){
        console.log('test 1');
        return (
            <React.Fragment>
                <Team name="Lucky Charms" logo='/src/img/lc.png' />
                <Game name="Lucky Charms" logo='/src/img/lc.png' venue='The Staple Center' />
            </React.Fragment>
            )
    }
}
ReactDOM.render(<App />, document.getElementById('root')) 
