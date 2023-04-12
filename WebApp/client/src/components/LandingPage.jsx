import { React, Component } from 'react'

export default class LandingPage extends Component {
    render() {
        return (
            <div className='content'>
                <h1>Welcome To the Page Brah</h1>
                <div className='search-area'>
                    <h1>Search for a video, Give me the link</h1>
                </div>
                <div className='emotion-display-area'>
                    <h1>Emotions here</h1>
                </div>
                <div className='keywords-display-area'>
                    <h1>keywords found in comment section</h1>
                </div>
                <div className='summary-display-area'>
                    <h1>Summary of the comment section</h1>
                </div>
                <div className='specific-summary-display-area'>
                    <h1>Summary about keywords, NEs etc</h1>
                </div>
            </div>
        );
    }
}