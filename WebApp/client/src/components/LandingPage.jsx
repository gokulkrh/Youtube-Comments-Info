import { React, Component } from 'react'
import ReactCardCarousel from "react-card-carousel";
import './styles/search-area.css'
import './styles/emo-stuff.css'
import './styles/summary.css'
import './styles/keywords.css'
import emo_info from "./cards.json"

export default class LandingPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: null
        };
    }

    fetchAllData = async () => {
        // const input = document.querySelector('.main-search-box');
        // var inp = input.value;
        // const videoid = inp.match(/v=([a-zA-Z0-9_-]{11})/)[1];

        // const url = "http://localhost:5000/fyp/v1/all/" + videoid;
        const url = "http://localhost:5000/fyp/v1/all/mock/fdgsdfg"
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
                <div className='search-area'>
                    <h1>Enter a video link</h1>
                    <div className="main-search-bar">
                        <input type="text" className="main-search-box"></input>
                        <button className="main-search-button" onClick={this.fetchAllData}>Search</button>
                    </div>
                </div>
                {this.state.data && (
                <>
                    <div className='emotions'>
                        <h1 className='section-title'>Emotions expressed in comments</h1>
                        <div className='emotion-display-carousel'>
                            <ReactCardCarousel>
                            {Object.entries(this.state.data.Emostats).map(([emotion, value]) => (
                                <div className='emo-cards' key={emotion}>
                                    <h1>{emotion}</h1>
                                    <img className='emo' src={require("./emopics/" + emo_info[emotion].filename)} alt='img'/>
                                    <p>{value.toFixed(2)} {emo_info[emotion].description}</p>
                                </div>
                            ))}
                            </ReactCardCarousel>
                        </div>
                    </div>
                    <div className='emotion-display-area'>
                        <h1 className='section-title'>Keywords found in comment section</h1>
                        {Object.entries(this.state.data.Keywords).map(([entity]) => (
                            <div key={entity}>
                                <button className='emotion-display'>{entity}:</button>
                            </div>
                        ))}
                    </div>
                    <div className='summary-display-area'>
                        <h1 className='section-title'>Summary of the comment section</h1>
                        <div className='summary-div'>
                            <span className='summary'>{this.state.data.Summary}:</span>
                        </div>
                    </div>
                </>
                )}
            </div>
        );
    }
}