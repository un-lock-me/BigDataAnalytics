import React from 'react';
import ReactDOM from 'react-dom';
import Welcome from './welcome';
import CustomComponent from './customComponent';

class MainApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: []
    };
    this.updateState = this.updateState.bind(this);
  }

  updateState(data) {
    this.setState((prevState) => ({
      data: data
    }));
  }

  componentDidMount() {
    let source = new EventSource('https://image-details.herokuapp.com/redirect');
    let that = this;
    let server_data = [];
    // console.log(source);
    source.onopen = function (e) {console.log(e)};
    source.onmessage = function (e) {
      // console.log(e);
    if(e.data != "" && server_data !== e.data){
      // console.log(e.data);
      // console.log("~~~~~~ New Data ~~~~~~~~");
      // console.log(server_data);
      server_data = e.data; 
      that.updateState(JSON.parse(server_data));
    }
    // console.log("Same data");
    // console.log(server_data);
      // console.log(JSON.parse(e.data));
    }
    source.onerror = function (e) {
      console.log(e)
    }
  }

  render() {
    if (this.state.data.length == 0 || this.state.data.data == " ")  {
      return (<Welcome/>);
    }
    return (<CustomComponent data={this.state.data}/>);
  }
}

ReactDOM.render(
  <MainApp/>, document.getElementById('app'));
