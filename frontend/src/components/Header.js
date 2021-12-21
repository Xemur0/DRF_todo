import React, {Component} from 'react';
import {Navbar, NavbarBrand, NavLink} from "reactstrap";

import logo from './logo192.png'


class Header extends Component {

    render() {
        return (

            <Navbar className={'navtop'}>



                <NavbarBrand href="/">
                    <img src={logo}
                         height='30'
                         width='30'
                         alt='logo'/>
                </NavbarBrand>
                <NavLink href="/users">Users</NavLink>
                <NavLink href="/project">Projects</NavLink>
                <NavLink href="/todo">ToDoList</NavLink>


            </Navbar>


        );
    }
}

export default Header;


