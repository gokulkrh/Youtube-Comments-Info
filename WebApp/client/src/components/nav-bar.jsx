import { React, Component } from "react";
import { Link } from "react-router-dom";
import "./styles/nav-bar.css"


export default class NavBar extends Component{
    render() {
        return(
            <header className="nav-bar">
                <div className="nav-container">
                    <ul>
                        <li>
                            <Link>Home</Link>
                            <Link>Emotions</Link>
                            <Link>Keywords</Link>
                            <Link>Summary</Link>
                            <Link>Detailed Summary</Link>
                        </li>
                        <div className="nav-search-bar">
                            <input type="text"></input>
                            <button className="search-button">Search</button>
                        </div>
                    </ul>
                </div>
            </header>
        );
    }
}