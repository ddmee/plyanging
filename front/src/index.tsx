import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Clock from './Clock';
import reportWebVitals from './reportWebVitals';


function Welcome(props: any) {
  return <h1>hello {props.name} </h1>;
}

// Get a list of books available to read. Display as a clickable list
// Click on the book, navigates to the text of the book.

function BookList(props: any) {
  const books = props.books;
  const bookList = books.map((book:string) =>
    <li key={book}>
      {book}
    </li>
  );
  return (
    <ul>{bookList}</ul>
  );
}


// load the list of books from the server api route
// make a get request to the book get endpoint
const books = ['The Last Kingdom', 'Things a Little Bird Told Me', 'Marked for Death'];


function tick() {
  ReactDOM.render(
    <React.StrictMode>
      <Clock />
      <Welcome name='roboto' />
      <BookList books={books} />
    </React.StrictMode>,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
