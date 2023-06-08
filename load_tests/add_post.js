import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 10, // Кількість одночасних користувачів (віртуальних користувачів)
  duration: '30s', // Тривалість тесту
};

export default function () {
  // Користувач авторизується у блозі
  login();

  // Створює новий допис
  createNewPost();

  // Вихід із блогу
  logout();
}

function login() {
  const url = 'http://localhost:8000/account/login';
  const payload = {
    username: 'new5_user_for_12553@gmail.com',
    password: 'asdf@1234',
  };
  const headers = {
    'Content-Type': 'application/json',
  };

  http.post(url, JSON.stringify(payload), { headers });

  // Очікування перед наступним кроком
  sleep(1);
}

function createNewPost() {
  const url = 'http://localhost:8000/post';
  const payload = {
    title: 'Назва нового допису',
    content: 'Текст нового допису...',
  };
  const headers = {
    'Content-Type': 'application/json',
  };

  http.post(url, JSON.stringify(payload), { headers });

  // Очікування перед наступним кроком
  sleep(1);
}

function logout() {
  const url = 'http://localhost:8000/account/logout';

  http.get(url);

  // Очікування перед наступним кроком
  sleep(1);
}
