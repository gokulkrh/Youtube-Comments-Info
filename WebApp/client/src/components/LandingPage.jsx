import { React, Component } from 'react'
import './styles/search-area.css'

export default class LandingPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: null
        };
    }

    fetchAllData = async () => {
        const input = document.querySelector('.main-search-box');
        var inp = input.value;
        const videoid = inp.match(/v=([a-zA-Z0-9_-]{11})/)[1];

        const url = "http://localhost:5000/fyp/v1/all/" + videoid;
        const response = await fetch(url, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        this.setState({ data });
        console.log(data)
    };
    render() {
        return (
            <div className='content'>
                {/* <h1>Welcome To the Page Brah</h1> */}
                <div className='search-area'>
                    <h1>Enter a video link</h1>
                    <div className="main-search-bar">
                        <input type="text" className="main-search-box"></input>
                        <button className="main-search-button" onClick={this.fetchAllData}>Search</button>
                    </div>
                </div>
                {this.state.data && (
                <>
                    <div className='emotion-display-area'>
                        <h1>Emotions expressed by viewers</h1>
                        {Object.entries(this.state.data.Emostats).map(([emotion, value]) => (
                            <div key={emotion}>
                                <button className='emotion-display'>{emotion}:</button>
                                <button className='emotion-display'>{value.toFixed(2)}</button>
                            </div>
                        ))}
                    </div>
                    <div className='emotion-display-area'>
                        <h1>Keywords found in comment section</h1>
                        {Object.entries(this.state.data.Keywords).map(([entity]) => (
                            <div key={entity}>
                                <button className='emotion-display'>{entity}:</button>
                            </div>
                        ))}
                    </div>
                    <div className='emotion-display-area'>
                        <h1>Summary of the comment section</h1>
                        <div className='summary-div'>
                            <span className='summary'>{this.state.data.Summary}:</span>
                        </div>
                    </div>
                </>
                )};
            </div>
        );
    }
}