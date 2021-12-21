import React from "react";
import {Link} from "react-router-dom";

const ProjectItem = ({project, deleteProject}) => {
    return (

        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.url_rep}</td>
            <td>{project.users}</td>
            <td>
                <button onClick={() => deleteProject(project.id)} type="button"> Delete</button>
            </td>

        </tr>
    )
}


const ProjectList = ({projects, deleteProject}) => {
    return (
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Url_rep</th>
            <th>Users</th>

            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}

            <Link to='/project/create'> Create </Link>
        </table>

    )
}
export default ProjectList;