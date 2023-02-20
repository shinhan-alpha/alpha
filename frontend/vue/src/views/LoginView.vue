<template>
  <div id="login-page">
    <div id="login-form">
      <img src="../../../images\shinhan_ci.jpg" style="width:350px; height:100px;" alt="My Image">
      <h2>신한투자증권 로그인</h2>
      <form @submit.prevent="fnLogin">
        <div>
          <input type="text" name="uid" placeholder="아이디" v-model="user_id">
        </div>
        <div>
          <input type="password" name="password" placeholder="비밀번호" v-model="user_pw">
        </div>
        <div>
          <button type="submit">로그인</button>
        </div>
        <div class="forgot-password">
          <a href="#">비밀번호 찾기</a>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_id: '',
      user_pw: ''
    }
  },
  methods: {
    fnLogin() {
      if (this.user_id === '') {
        alert('아이디를 입력하시오')
        return
      }
      if (this.user_pw === '') {
        alert('비밀번호를 입력하시오')
        return
      }
      alert('로그인 성공!')
    }
  }
}
</script>

<style>
#login-page {
  background-image: url('https://cdn.pixabay.com/photo/2015/09/04/23/22/facebook-923828_1280.jpg');
  background-size: cover;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

#login-form {
  background-color: #fff;
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

h2 {
  font-size: 28px;
  margin-bottom: 20px;
  color: #1877f2;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  height: 50px;
  border-radius: 5px;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 18px;
}

button {
  background-color: #1877f2;
  color: #fff;
  border: none;
  border-radius: 5px;
  height: 50px;
  font-size: 20px;
  cursor: pointer;
  width: 100%;
}

.forgot-password {
  margin-top: 20px;
  text-align: center;
}

a {
  color: #1877f2;
  text-decoration: none;
}
</style>
