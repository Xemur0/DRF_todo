import React from "react";


class TodoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            project: 0,
            text: '',
            creator: 0,
            is_active: '',
        }
    }

    handleChange(event) {
        const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
        this.setState(
            {
                [event.target.name]: value
            }
        )
    }

    handleSubmit(event) {
        console.log(this.state.project + ' ' + this.state.text + ' ' + this.state.creator + ' ' + this.state.is_active)
        this.props.createTodo(this.state.project, this.state.text, this.state.creator, this.state.is_active)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div className="form-group">
                    <label htmlFor="text">Text</label>
                    <input type="text" className="form-control" name="text" value={this.state.text}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label htmlFor="project">Project</label>

                    <select name="project" multiple onChange={(event) => this.handleChange(event)}>
                        {this.props.projects.map((item) => <option value={item.id}>{item.name}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="creator">Creator</label>
                    <select name="creator" multiple onChange={(event) => this.handleChange(event)}>
                        {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                </div>
                <div>
                    <label>Is_active</label>
                    <input type='checkbox' name='is_active' onChange={(event) => this.handleChange(event)}/>
                </div>


                <input type="submit" value="Save"/>
            </form>
        );
    }


}

export default TodoForm;