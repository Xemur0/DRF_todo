import './App.css';
import React from 'react'
import axios from "axios";
import UserList from "./components/User";
import Header from "./components/Header";
import Footer from "./components/Footer";
import {Route, BrowserRouter} from "react-router-dom";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(
            response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }
        ).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/project/').then(
            response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }
        ).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/').then(
            response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }
        ).catch(error => console.log(error))
    }

    render() {
        return (

            <div>
                <Header/>
                <BrowserRouter>
                    <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                    <Route exact path='/project' component={() => <ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}/>}/>

                </BrowserRouter>
                <Footer/>
            </div>

        );
    }

}

export default App;
