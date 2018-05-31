import React, { Component } from 'react';
import logo from './logo.svg';
import './App.scss';
import Main from "./pages/Main/Main"
import Register from "./pages/Register/Register"
import Login from "./pages/Login/Login"
import FontAwesome from 'react-fontawesome';
import Header from './components/header/header'
var net = require("./services/network")

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      hasLogin: false,
      loging: false,
      registering: true
    }
  }

  componentWillMount() {
    //查询是否已登录
    net.getUser()
      .then(ret => ret.json())
      .then(json => {
        console.log(json);
        if (json.code == 0) {
          this.setState({
            hasLogin: true,
            registering: false
          })
        }
      })
      .catch(e => console.log(e))
  }

  logOutHandler = () => {
    net.logout()
    .then(res => res.json())
    .then(json => {
      if (json.code == 0) {
        this.setState({
          hasLogin: false,
          loging: true
        })
      } else {
        alert("登出失败，请稍后再试");
      }
    }).catch(e => console.error(e));
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
        <Header logOutHandler={this.logOutHandler}/>
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
