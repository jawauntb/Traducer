import React, { Component } from 'react';
import translate from './translate.svg';
import './App.css';
import ReactDOM from 'react-dom';

class App extends Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
    this.state = {
      value: -1
    };
  }

  handleClick () {
      this.setState({value: (-1*this.state.value)});
  }

  render () {
    if (this.state.value === -1){
      return(
        <div>
          <nav>
            <div id="nav">          
            <img src={translate}></img>
              <span>Traduce: the translation nation's number 1 notes board </span>
                <div id="choices" className="wideDiv">
                  <button onClick={this.handleClick}>See History</button>
                </div>
            </div>
          </nav>
          <div>
            <TextForm />
          </div>
        </div>
      );
    }

    if (this.state.value === 1){
      return (
        <div>
          <nav>
          <div id="nav">          
            <img src={translate}></img>
              <span>Traduce: the translation nation's number 1 notes board </span>
                <div id="choices" className="wideDiv">
              <button onClick={this.handleClick}>Translate</button>
              </div>
            </div>
          </nav>
          <div>
            <Table />
          </div>
        </div>
      );
    }
  }
}


class TextForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 'Please enter a new phrase.'
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    var text_in = JSON.stringify({
      input_text: this.state.value,
      language: "",
      output_text: ""
    });
    alert('A New Phrase Was Submitted For Translation: ' + this.state.value);
    fetch('http://127.0.0.1:8000/api/translations/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: text_in
    });
  }

  render() {
    return (
      <form id="entry" onSubmit={this.handleSubmit}>
      
        <label> 
          <div>
            Enter Your Foreign Language Text Here:
            <span></span>  
          </div>
          <span></span>  
          <textarea value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

// export default TextForm;


class Table extends Component {
  state = {
    translations: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/translations/');
      const translations = await res.json();
      this.setState({
        translations
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <table id="entries">
        <tr>
            <td>Entered Text</td>
            <td>Language of Input</td>
            <td>English Translation</td>
        </tr>
       {this.state.translations.map(item => (
        <tr>
          <td key={item.input_text}>{item.input_text}</td>
          <td key={item.language}>{item.language}</td>
          <td key={item.output_text}>{item.output_text}</td>
        </tr>
      ))}
      </table>
    );
  }
}


export {App, TextForm, Table};
