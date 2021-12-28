import './App.css';
import React from 'react'
import axios from "axios";
import UserList from "./components/User";
import Header from "./components/Header";
import Footer from "./components/Footer";
import {Route, BrowserRouter, Link} from "react-router-dom";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import LoginForm from "./components/LoginForm";
import Cookies from "universal-cookie/lib";
import {Button} from "reactstrap";
import ProjectForm from "./components/projectForm"
import TodoForm from "./components/TodoForm";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': '',
            'username': ''
        }
    }

    createProject(name, url, users) {
        const headers = this.get_headers()
        const data = {name: name, url_rep: url, users: users}
        axios.post(`http://127.0.0.1:8000/api/project/`, data, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }

    createTodo(project, text, creator, is_active) {
        const headers = this.get_headers()
        const data = {project: project, text: text, creator: creator, is_active: is_active}
        console.log(data)
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    deleteToDo(id) {

        const headers = this.get_headers()

        axios.delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    deleteProject(id) {
        const headers = this.get_headers()
        console.log(headers)
        axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers}).then(
            response => {
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }

    set_token(token) {
        console.log(token)
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    set_username(username) {
        const cookies = new Cookies()
        cookies.set('username', username)
        this.setState({'username': username})
    }

    is_auth() {
        return !!this.state.token
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {

        const cookies = new Cookies()
        const token = cookies.get('token')
        const username = cookies.get('username')
        this.setState({'token': token}, () => this.load_data())
        this.setState({'username': username})
    }


    get_token(username, password) {
        const data = {username: username, password: password}
        axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(
            response => {
                this.set_token(response.data['token'])
                this.set_username(username)

                console.log(response.data)
                // cookies.set('token', response.data)
            }
        ).catch(error => alert('Wrong login or password'))

    }

    load_data() {
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(
            response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({users: []})
        })


        axios.get('http://127.0.0.1:8000/api/project/', {headers}).then(
            response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })

        axios.get('http://127.0.0.1:8000/api/todo/', {headers}).then(
            response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (

            <div>
                <Header/>


                <BrowserRouter>
                    <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                    <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}
                                                                         deleteToDo={(id) => this.deleteToDo(id)}/>}/>
                    <Route exact path='/project' component={() => <ProjectList projects={this.state.projects}
                                                                               deleteProject={(id) => this.deleteProject(id)}/>}/>


                    <Route exact path='/todo/create'
                           component={() => <TodoForm users={this.state.users} projects={this.state.projects}
                                                      createTodo={(project, text, creator, isActive) => this.createTodo(project, text, creator, isActive)}/>}/>

                    <Route exact path='/login' component={() => <LoginForm
                        get_token={(username, password) => this.get_token(username, password)}/>}/>


                    <Route exact path='/project/create/'
                           component={() => <ProjectForm users={this.state.users}
                                                         createProject={(name, url, users) => this.createProject(name, url, users)}/>}/>


                    {/*<Navbar>*/}
                    <div className={'button_login'}>
                        <Button>
                            {this.is_auth() ? <div> {this.state.username + ' '}
                                    <Button onClick={() => this.logout()}> Выйти
                                    </Button></div> :
                                <Link to='/login'> Войти</Link>}
                        </Button>
                    </div>


                    {/*</Navbar>*/}
                </BrowserRouter>
                <Footer/>
            </div>

        );
    }

}

export default App;
