import React from "react";


class projectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            url: '',
            users: [],
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleUsersChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'users': []
            })
            return;
        }
        let usersList = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            usersList.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'users': usersList
        })
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.url, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div className="form-group">
                    <label htmlFor="name">Name</label>
                    <input type="text" className="form-control" name="name" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <div className="form-group">
                    <label htmlFor="url">Url</label>
                    <input type="text" className="form-control" name="url" value={this.state.url}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="users">users</label>
                    <select name="author" multiple onChange={(event) => this.handleUsersChange(event)}>
                        {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                    </select>
                </div>


                <input type="submit" value="Save"/>
            </form>
        );
    }
}

export default projectForm;