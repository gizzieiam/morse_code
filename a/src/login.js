
import './login.css'

function Login(props){
    let [toggle, setToggle] = useState(true)

    function handleToggle() {
        let log = document.getElementById('login-form')
        let reg = document.getElementById('register-form')
        
        if(toggle === true){
        log.style.display='none'
        reg.style.display='block'
        setToggle(toggle = false)
        }else{
            reg.style.display='none'
            log.style.display='block'
            setToggle(toggle = true)
        }
    }

    return(
        <>
            <form id='login-form'>
            <h1>{props.greeting}</h1>
                <label for='email'>Email</label>
                <input id='email' />
                <label for='password'>Password</label>
                <input id='password' />
                <button type='submit' class='submit-btn'>Log in</button>
                <p>
                    Dont have an account?
                        <button className='toggle-btn' onClick={handleToggle}>
                        Register
                        </button>
                </p>
            </form>
            <form id='register-form'>
                <h1 id='welcome'>{props.signup}</h1>
                <section id='section-one'>
                    <label>Username</label>
                    <input id='username' />
                    <label>Name</label>
                    <input id='name' />
                    <label>Email</label>
                    <input id='new-email' />
                    <label>Password</label>
                    <input id='new-password' />
                    <button type='submit' className='submit-btn'>Register</button>
                <p>
                    Already have an account?
                        <button className='toggle-btn' onClick={handleToggle}>
                        Login
                        </button>
                </p>
                </section>
                <section id='section-two'>
                    <h3 id='quarter'>What Quarter are you in?</h3>
                    <button className='q-btn'>Q1</button>
                    <button className='q-btn'>Q2</button>
                    <button className='q-btn'>Q3</button>
                    <button className='q-btn'>Q4</button>
                    <br />
                    <button>Coach</button>
                    <button>Student</button>
                </section>
                
            </form>
        </>
    )
}


export default Login