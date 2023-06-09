import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {

  stages: [
    { duration: '1m', target: 100 },  // Поступово збільшуємо навантаження до 100 користувачів
    { duration: '15s', target: 150 },  // // Поступово збільшуємо навантаження до 200 користувачів
    { duration: '15s', target: 200 },  // // Поступово збільшуємо навантаження до 300 користувачів
    { duration: '15s', target: 250 },  // // Поступово збільшуємо навантаження до 400 користувачів
    { duration: '15s', target: 100},  // // Поступово збільшуємо навантаження до 500 користувачів
    { duration: '1m', target: 0 },    // Повільно зменшуємо навантаження до 0 користувачів
  ],
};
export function setup() {
  const addTestDataResponse = http.get('https://27b6-194-146-228-24.ngrok-free.app/create-test-data');

  check(addTestDataResponse, {
    'Add test data status is 200': (res) => res.status === 200,
  });
}

// Видалення тестових даних після тесту
export function teardown() {
  const deleteTestDataResponse = http.get('https://27b6-194-146-228-24.ngrok-free.app/clean-test-data');

  check(deleteTestDataResponse, {
    'Delete test data status is 200': (res) => res.status === 200,
  });
}

export default function () {
  // Авторизація користувача
  const loginResponse = http.post('https://27b6-194-146-228-24.ngrok-free.app/account/login', {
    username: 'new5_user_for_12553@gmail.com',
    password: 'asdf@1234',
  });

  check(loginResponse, {
    'Login status is 200': (res) => res.status === 200,
  });

  // Отримання повного тексту останнього допису
  const blogPostResponse = http.get('https://27b6-194-146-228-24.ngrok-free.app/post_detail/25');
  // const blogPostResponse = http.get('http://127.0.0.1:8000//post_detail/25');

  check(blogPostResponse, {
    'Blog post status is 200': (res) => res.status === 200,
  });

  // Вихід із блогу (розлогінення)
  const logoutResponse = http.get('https://27b6-194-146-228-24.ngrok-free.app/account/logout/');
  // const logoutResponse = http.get('http://127.0.0.1:8000/account/logout');

  check(logoutResponse, {
    'Logout status is 200': (res) => res.status === 200,
  });

  // Затримка перед наступним запитом
  sleep(1);
}
// import http from 'k6/http';
// import { sleep, check } from 'k6';
//
// export const options = {
//   vus: 10, // Кількість одночасних користувачів (віртуальних користувачів)
//   duration: '30s', // Тривалість тесту
//   // stages: [
//   //   { duration: '1m', target: 100 },  // Поступово збільшуємо навантаження до 100 користувачів
//   //   { duration: '15s', target: 200 },  // // Поступово збільшуємо навантаження до 200 користувачів
//   //   { duration: '15s', target: 300 },  // // Поступово збільшуємо навантаження до 300 користувачів
//   //   { duration: '15s', target: 400 },  // // Поступово збільшуємо навантаження до 400 користувачів
//   //   { duration: '15s', target: 500 },  // // Поступово збільшуємо навантаження до 500 користувачів
//   //   { duration: '1m', target: 0 },    // Повільно зменшуємо навантаження до 0 користувачів
//   // ],
// };
//
// export default function () {
//   // Авторизація користувача
//   const loginResponse = http.post('https://27b6-194-146-228-24.ngrok-free.app/account/login', {
//     username: 'new5_user_for_12553@gmail.com',
//     password: 'asdf@1234',
//   });
//
//   check(loginResponse, {
//     'Login status is 200': (res) => res.status === 200,
//   });
//
//   // Отримання повного тексту останнього допису
//   const blogPostResponse = http.get('https://27b6-194-146-228-24.ngrok-free.app/post_detail/25');
//
//   check(blogPostResponse, {
//     'Blog post status is 200': (res) => res.status === 200,
//   });
//
//   // Вихід із блогу (розлогінення)
//   const logoutResponse = http.get('https://27b6-194-146-228-24.ngrok-free.app/account/logout');
//
//   check(logoutResponse, {
//     'Logout status is 200': (res) => res.status === 200,
//   });
//
//   // Затримка перед наступним запитом
//   sleep(1);
// }
