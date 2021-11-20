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
                        width='30'/>
                    </NavbarBrand>

                    <NavLink href="/home">Home</NavLink>
                    <NavLink href="/contacts">Contacts</NavLink>

            </Navbar>
        );
    }
}

export default Header;


