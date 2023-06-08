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
  updateProfile();

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

function updateProfile() {
  const url = 'http://127.0.0.1:8000/profile_edit/41/';
  const payload = {
    name: 'New Name',
    lastname: 'New Lastname',
    age: '33',
    website: 'http://example1.com',
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
