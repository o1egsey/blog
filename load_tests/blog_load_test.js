import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 10, // Кількість одночасних користувачів (віртуальних користувачів)
  duration: '30s', // Тривалість тесту
};

export default function () {
  // Авторизація користувача
  const loginResponse = http.post('http://localhost:8000/account/login', {
    username: 'new5_user_for_12553@gmail.com',
    password: 'asdf@1234',
  });

  if (loginResponse.status === 200) {
    console.log('Login successful');
  } else {
    console.log('Login failed');
  }

  // Отримання повного тексту останнього допису
  const blogPostResponse = http.get('http://localhost:8000/post_detail/25');
  if (blogPostResponse.status === 200) {
    console.log('Blog viewed successful');
  } else {
    console.log('Fail to view blog');
  }

  // Вихід із блогу (розлогінення)
  const logoutResponse = http.get('http://localhost:8000/account/logout');

  if (logoutResponse.status === 200) {
    console.log('Logout successful');
  } else {
    console.log('Logout failed');
  }

  // Затримка перед наступним запитом
  sleep(1);
}
