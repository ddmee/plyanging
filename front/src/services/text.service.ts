import http from './http_common';

export interface TextObj {
  id: number;
  text: string;
  creation_datetime: string;
  created_by: string;
}

export function getTextAll() {
  return http.get('Text/');
}
