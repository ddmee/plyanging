import React from 'react';
import { useParams } from 'react-router-dom';
import { getPhraseAll, PhraseObj } from '../services/phrase.service';

type PhraseSelectProps = {
  textId: number;
};

type PhraseSelectState = {
  getPhraseAll: PhraseObj[];
}

/**
* Presents a horizontally scrolling selection of phrases.
* Click on the phrase to begin reading it.
 */
class PhraseSelectCls extends React.Component<PhraseSelectProps, PhraseSelectState> {
  state: PhraseSelectState = {
    getPhraseAll: [],
  }

  componentDidMount() {
    getPhraseAll(this.props.textId).then(
      response => {
        this.setState({ getPhraseAll: response.data});
      }
    )
  }

  render() {
    const PhraseSelect = this.state.getPhraseAll.map((phrase:PhraseObj) =>
      <li key={phrase.pk}>
        <p>{phrase.phrase}</p>
      </li>
    );
    return (
      <ul>{PhraseSelect}</ul>
    );
  }
}

// to allow this.props.match.params.id to get the parameters instead of using
// useParams() which cannot be used in a class component.
// See https://stackoverflow.com/a/58636280/4498470
// The withRouter() no longer works in react-router-dom v6.
// Easiest thing is to wrap the class in a function, using useParams() in the
// function and feeding the params as a prop to the class component.
// See https://stackoverflow.com/a/60055137/4498470
export default function PhraseSelect() {
  let params = useParams();
  return (
    <PhraseSelectCls textId={Number(params.textId)} />
  );
}
