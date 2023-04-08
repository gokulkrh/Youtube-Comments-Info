import { React, Component } from 'react'
import { Link } from 'react-router-dom';
import './styles/footer.css'
import github_icon from './icons/github2.png';
import youtube_icon from './icons/youtube.png'
import twitter from './icons/twitter.png'
import instagram from './icons/instagram.png'
import Contact from './contact';


export default class Footer extends Component{
    render() {
        return (
            <div className='footer'>
                <div className='footer-column'>
                    <div className='footer-about-section'>
                        <p>
                            About: <br />
                            Extracting Audience Feedback from User Comments using multilabel Emotion recognition and Text Summarization <br />
                            Final Year Project group 10b <br />
                            Gokul Krishnan G <br />
                            AM.EN.U4CSE19321 <br />
                        </p>
                    </div>
                    <div className='socials'>
                        <div className='media-link-icons'>
                            <h3>Find me:</h3>
                            <Link><img className='footer-media-icons' src={github_icon} alt="" /></Link>
                            <Link><img className='footer-media-icons' src={youtube_icon} alt="" /></Link>
                            <Link><img className='footer-media-icons' src={twitter} alt="" /></Link>
                            <Link><img className='footer-media-icons' src={instagram} alt="" /></Link>
                        </div>
                    </div>
                    <Contact />
                </div>
                <div className='disclaimer'>
                    <p>
                        Please Note: The content displayed by the website is auto-generated using publicly available data such as comments.<br />
                        Any crass or offensive content displayed by the website is purely coincidental.<br />
                        They are not a representation of the website creator's beliefs or views.
                    </p>
                </div>
            </div>
        );
    }
}