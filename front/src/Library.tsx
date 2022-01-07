import React from 'react';
import ReactDOM from 'react-dom';
import './Library.css';
import axios from 'axios';
import { API_URL } from './constants';

// const axios = require('axios');

// Get a list of books available to read. Display as a clickable list
// Click on the book, navigates to the text of the book.

function TextList(props: any) {
  const textAll:TextObj[] = props.getTextAll;
  const textList = textAll.map((text:TextObj) =>
    <li key={text.id}>
      <p>Text: {text.text.slice(0,20)}</p>
      <p>Creation Date: {text.creation_datetime}</p>
      <p>User: {text.created_by}</p>
    </li>
  );
  return (
    <ul>{textList}</ul>
  );
}

interface TextObj {
  id: number;
  text: string;
  creation_datetime: string;
  created_by: string;
}

type LibraryProps = {};

type LibraryState = {
  getTextAll: TextObj[];
}

export default class Library extends React.Component<LibraryProps, LibraryState> {
  state: LibraryState = {
    getTextAll: [],
  }

  componentDidMount() {
    axios.get(API_URL + 'Text/').then(
      response => {
        this.setState({ getTextAll: response.data});
      }
    )
  }

  render() {
    return (
      <div>
        <h1>Library</h1>
        <input type='search' placeholder='Search'/>
        <TextList getTextAll={this.state.getTextAll} />
       </div>
    );
  }

}