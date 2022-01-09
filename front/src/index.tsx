import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import './index.css';
import App from './App';
import LibraryPage from './routes/LibraryPage';
import LoginPage from './routes/LoginPage';
import NotFound from './routes/NotFound';
import TextPage from './routes/TextPage';
import reportWebVitals from './reportWebVitals';


ReactDOM.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route path="LibraryPage" element={<LibraryPage />} />
        <Route path="LoginPage" element={<LoginPage />} />
        <Route path="Text/:textId" element={<TextPage />} />
      </Route>
      <Route path="*"  // * will only match when no other routes do.
      // no url match route.
        element={<NotFound />}
      />
    </Routes>
  </BrowserRouter>,
  document.getElementById('root')
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
