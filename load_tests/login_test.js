import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  const url = 'http://localhost:8000/account/login';
  const payload = {
    username: 'new5_user_for_12553@gmail.com',
    password: 'asdf@1234',
  };
  const headers = {
    'Content-Type': 'application/json',
  };

  const response = http.post(url, JSON.stringify(payload), { headers });

  // Check the response to validate the login
  if (response.status === 200) {
    console.log('Login successful');
  } else {
    console.log('Login failed');
    console.log(response.body);
  }

  // Wait for a short duration before proceeding to the next step
  sleep(1);
}
