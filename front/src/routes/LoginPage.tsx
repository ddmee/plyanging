import NavBar from '../components/NavBar';


export default function LoginPage() {
    return (
        <div>
          <NavBar />
          <h1>Login</h1>
          <input type="email" placeholder="email" />
          <input type="password" />
          <input type="submit" />
        </div>
    );
}