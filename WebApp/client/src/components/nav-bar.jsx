import { React, Component } from "react";
import "./styles/nav-bar.css"


export default class NavBar extends Component{
    render() {
        return(
            <header className="nav-bar">
                <div className="nav-container">
                    <ul>
                        <li>
                            <button className="nav-buttons">Home</button>
                            <button className="nav-buttons">Emotions</button>
                            <button className="nav-buttons">Keywords</button>
                            <button className="nav-buttons">Summary</button>
                            <button className="nav-buttons">Detailed Summary</button>
                        </li>
                        {/* <div className="nav-search-bar">
                            <input type="text" className="nav-search-box"></input>
                            <button className="search-button">Search</button>
                        </div> */}
                    </ul>
                </div>
            </header>
        );
    }
}