<template>
  <div class="signup-page-container">
    <img src="../../../images\shinhan_ci.jpg" style="width:350px; height:100px;" alt="My Image">
    <h2>신한투자증권 회원가입</h2>
    <form class="signup-form">
      <div class="form-group">
        <label for="username">이름</label>
        <input type="text" class="form-control" v-model="username" placeholder="이름" />
      </div>
      <div class="form-group">
        <label for="tel">전화번호</label>
        <input type="text" class="form-control" v-model="tel" placeholder="전화번호" />
      </div>
      <div class="form-group">
        <label for="password">비밀번호</label>
        <input type="password" class="form-control" v-model="password" placeholder="비밀번호" />
      </div>
      <div class="form-group">
        <label for="password_check">비밀번호 재입력</label>
        <input type="password" class="form-control" v-model="password_check" placeholder="비밀번호 재입력" />
      </div>
      <button type="button" class="btn btn-primary signup-btn" @click="login">회원가입</button>
      <div class="terms">
        By clicking Sign Up, you agree to our <a href="#">Terms</a>, <a href="#">Data Policy</a> and <a href="#">Cookie
          Policy</a>. You may receive SMS notifications from us and can opt out at any time.
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'SignupView',
  data() {
    return {
      username: "",
      tel: "",
      password: "",
      password_check: "",
    };
  },
  methods: {
    login() {
      if (this.password !== this.password_check) {
        alert("Passwords do not match");
        return;
      }

      const data = {
        username: this.username,
        tel: this.tel,
        password: this.password,
        password_check: this.password_check,
      };

      axios
        .post("http://127.0.0.1:8000/api/member", data)
        .then(() => {
          alert("Sign up successful!");
        })
        .catch((error) => {
          let errorMsg = "";

          if (error.response.data.password) {
            errorMsg += "Password error";
          }
          if (error.response.data.username) {
            errorMsg += "\nName error";
          }
          if (errorMsg) {
            alert(errorMsg);
          }
        });
    },
  },
};
</script>

<style>
.signup-page-container {
  width: 500px;
  margin: 50px auto;
}

h2 {
  font-size: 28px;
  margin-bottom: 20px;
  font-weight: bold;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  width: 100%;
  height: 50px;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
  font-size: 18px;
}

.signup-btn {
  width: 100%;
  height: 50px;
  border-radius: 5px;
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 15px;
}

.terms {
  font-size: 14px;
  margin-top: 15px;
  line-height: 1.5;
  color: #65676b;
}

.terms a {
  text-decoration: none;
  color: #385898;
  font-weight: bold;
}

.signup-btn:hover {
  background-color: #3367d6;
  border-color: #2a56c6;
}
</style>
