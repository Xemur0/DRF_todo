import React from "react";

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>

            <td>{todo.is_active}</td>
            <td>{todo.project}</td>
            <td>{todo.creator}</td>

        </tr>
    )
}


const ToDoList = ({todos}) => {
    return (
        <table>
            <th>ID</th>
            <th>text</th>
            <th>date_create</th>
            <th>date_update</th>
            <th>is_active</th>
            <th>project</th>
            <th>creator</th>

            {todos.map((todo) => <ToDoItem todo={todo}/>)}
        </table>
    )
}
export default ToDoList;