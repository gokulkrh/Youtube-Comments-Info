import { React, Component } from 'react'

export default class Contact extends Component {
    SendEmail(message) {
        if(message === "") {
            console.log("HEY type something")
        } else {
            console.log("email recieved..", message)
        }
    }
    render() {
        return (
            <div className='contact-details'>
                <textarea type="text" className='message-to-me' placeholder='type something....'/>
                <br />
                <button className='email-button' onClick={() => this.SendEmail(document.querySelector('.message-to-me').value)}>
                    Send a message
                </button>
            </div>
        );
    }
}