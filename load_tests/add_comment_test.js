import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 5, // Кількість одночасних користувачів (віртуальних користувачів)
  duration: '30s', // Тривалість тесту
};

export default function () {
  // Користувач авторизується у блозі
  const loggedIn = login();
  if (!loggedIn) {
    console.log('Login failed');
    return;
  }

  // Переглядає повний текст останнього запису
  const latestPostViewed = viewLatestPost();
  if (!latestPostViewed) {
    console.log('Failed to view latest post');
    return;
  }

  // Повертається на головну сторінку
  const homeVisited = goHome();
  if (!homeVisited) {
    console.log('Failed to go to home page');
    return;
  }

  // Відкриває інший запис
  const differentPostOpened = openDifferentPost();
  if (!differentPostOpened) {
    console.log('Failed to open different post');
    return;
  }

  // Залишає коментар
  const commentLeft = leaveComment();
  if (!commentLeft) {
    console.log('Failed to leave comment');
    return;
  }

  // Вихід із блогу
  const loggedOut = logout();
  if (!loggedOut) {
    console.log('Logout failed');
    return;
  }
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

  const response = http.post(url, JSON.stringify(payload), { headers });

  // Очікування перед наступним кроком
  sleep(1);

  return response.status === 200;
}

function viewLatestPost() {
  const url = 'http://localhost:8000/post_detail/25';

  const response = http.get(url);

  // Очікування перед наступним кроком
  sleep(1);

  return response.status === 200;
}

function goHome() {
  const url = 'http://localhost:8000';

  const response = http.get(url);

  // Очікування перед наступним кроком
  sleep(1);

  return response.status === 200;
}

function openDifferentPost() {
  const url = 'http://localhost:8000/post_detail/26';

  const response = http.get(url);

  // Очікування перед наступним кроком
  sleep(1);

  return response.status === 200;
}

function leaveComment() {
  const url = 'http://localhost:8000/post_detail/26';
  const payload = {
    content: 'Текст нового коментаря...',
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

  const response = http.get(url);

  // Очікування перед наступним кроком
  sleep(1);

  return response.status === 200;
}
