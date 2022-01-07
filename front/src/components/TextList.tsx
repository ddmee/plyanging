import React from 'react';
import './TextList.css';
import { getTextAll, TextObj } from '../services/text.service';

type TextListProps = {};

type TextListState = {
  getTextAll: TextObj[];
}

/**
* Get a list of books available to read. Display as a clickable list
* Click on the book, navigates to the text of the book.
 */
export default class TextList extends React.Component<TextListProps, TextListState> {
  state: TextListState = {
    getTextAll: [],
  }

  componentDidMount() {
    getTextAll().then(
      response => {
        this.setState({ getTextAll: response.data});
      }
    )
  }

  render() {
    const textList = this.state.getTextAll.map((text:TextObj) =>
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
}
