import { Link } from 'react-router-dom';


export default function NavBar() {
    return (<div>
        <nav>
            <Link to='/'>App</Link>
            <Link to='/LoginPage'>Login</Link>
            <Link to='/LibraryPage'>Library</Link>
        </nav>
    </div>
    );
}