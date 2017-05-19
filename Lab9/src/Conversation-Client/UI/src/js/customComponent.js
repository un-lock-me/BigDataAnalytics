import React from 'react';

class CustomComponent extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let rows = [];
        console.log(this.props.data.data);
        this.props.data.data.map((images, i) => rows.push(
                <a><div className="box"> <img className = "clipped" key={i} src={images}/> </div> </a>
            ));
        return (
            <div className="container">
                <div className="header"></div>
                    <div className="img-div">
                        {rows}
                    </div>
                <div className="footer"></div>
            </div>
        );
    }
}

export default CustomComponent;