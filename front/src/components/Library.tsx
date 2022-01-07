import React from 'react';
import ReactDOM from 'react-dom';
import './Library.css';
import TextList from './TextList';

type LibraryProps = {};

type LibraryState = {};

/**
 * Presents a library of text or book objects that a user can begin reading
 */
export default class Library extends React.Component<LibraryProps, LibraryState> {
  state: LibraryState = {}

  render() {
    return (
      <div className="library">
        <h1>Library</h1>
        <input type='search' placeholder='Search'/>
        <TextList />
       </div>
    );
  }
}
