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
        var url = input.value;
        url = "http://localhost:5000/fyp/v1/all/%3Cvideoid%3E";
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
                    <h1>Search for a video, Give me the link</h1>
                    <div className="main-search-bar">
                        <input type="text" className="main-search-box"></input>
                        <button className="main-search-button" onClick={this.fetchAllData}>Search</button>
                    </div>
                </div>
                {this.state.data && (
                <>
                    <div className='emotion-display-area'>
                        <h1>Emotions expressed by viewers</h1>
                        {Object.entries(this.state.data.EmoStats).map(([emotion, value]) => (
                            <div key={emotion}>
                                <span className='emotion-display'>{emotion}:</span>
                                <span className='emotion-display'>{value.toFixed(2)}</span>
                            </div>
                        ))}
                    </div>
                    <div className='keywords-display-area'>
                        <h1>Keywords found in comment section</h1>
                        {Object.entries(this.state.data.Entities).map(([entity]) => (
                            <div key={entity}>
                                <span className='entity-display'>{entity}:</span>
                            </div>
                        ))}
                    </div>
                    <div className='summary-display-area'>
                        <h1>Summary of the comment section</h1>
                    </div>
                    <div className='specific-summary-display-area'>
                        <h1>Summary about keywords, NEs etc</h1>
                    </div>
                </>
                )};
            </div>
        );
    }
}