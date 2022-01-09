import http from './http_common';

export interface PhraseObj {
  pk: number;
  phrase: string;
}

export function getPhraseAll(text_id:number) {
  return http.get(`Phrase/${text_id}`);
}
