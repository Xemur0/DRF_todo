import React from "react";
import {Link} from "react-router-dom";

const ToDoItem = ({todo, deleteToDo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.is_active ? <td>1</td> : <td>0</td>}</td>
            <td>{todo.project}</td>
            <td>{todo.creator}</td>
            <td>
                <button onClick={() => deleteToDo(todo.id)} type="button">
                    Active/Deactive
                </button>
            </td>

        </tr>
    )
}


const ToDoList = ({todos, deleteToDo}) => {
    return (
        <table>
            <th>ID</th>
            <th>text</th>
            <th>date_create</th>
            <th>date_update</th>
            <th>is_active</th>
            <th>project</th>
            <th>creator</th>
            <th></th>


            {todos.map((todo) => <ToDoItem todo={todo} deleteToDo={deleteToDo}/>)}
            <Link to='/todo/create'> Create </Link>
        </table>

    )
}
export default ToDoList;