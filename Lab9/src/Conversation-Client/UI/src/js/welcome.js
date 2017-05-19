import React from 'react';

class Welcome extends React.Component {
    render() {
        return (
            <div>
                <div className="container">
                    <div className="row vertical-center">
                        <h1>I'm your personal assistant - 'Genie!'</h1>
                        <h3>Ask me a question...</h3>
                        <div className="row top-margin">
                            <h5>Below questions are supported for now..</h5>
                            <div>Hey Genie.. Show me Horses?</div>
                            <div>Show me cat pictures?</div>
                            <div>Show me Dog photos?</div>
                            <div>Clear the screen</div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Welcome;
