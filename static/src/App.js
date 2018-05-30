import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Main from "./pages/Main/Main"
import Register from "./pages/Register/Register"
import Login from "./pages/Login/Login"
import FontAwesome from 'react-fontawesome';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      hasLogin: false,
      loging: false,
      registering: true
    }

  }

  goToLogin = () => {
    this.setState({
      registering: false,
      loging: true
    })
  }

  goToRegister = () => {
    this.setState({
      registering: true,
      loging: false
    })
  }

  LoginCallback = () => {
    this.setState({
      hasLogin: true,
      loging: false,
      registering: false
    })
  }

  registerCallback = () => {
    this.setState({
      registering: false,
      loging: true
    })
  }

  render() {

    //注册
    return (
      <div className="all">
        <div className="header">
          <FontAwesome name='bars' />
          <span>在线人体检测系统</span>
        </div>
        <div className="body">
          {(() => {
            if (!this.state.hasLogin && this.state.registering) {
              return (
                <Register
                  handleBack={this.goToLogin}
                  handleNext={this.registerCallback} />
              );
            }
            //登录
            if (!this.state.hasLogin && this.state.loging) {
              return (
                <Login
                  handleBack={this.goToRegister}
                  handleNext={this.LoginCallback} />
              );
            }
            //主页
            return (
              <Main />
            );
          })()}
        </div>
        <div className="footer">
        </div>
      </div>
    )
  }
}

export default App;
