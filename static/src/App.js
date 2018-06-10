import React, { Component } from 'react';
import logo from './logo.svg';
import './App.scss';
import Picture from "./pages/Picture/Picture";
import Video from './pages/Video/Video'
import User from './pages/User/User'
import Model from './pages/Model/Model'
import Register from "./pages/Register/Register";
import Login from "./pages/Login/Login";
import FontAwesome from 'react-fontawesome';
import Header from './components/header/header';
import Main from './pages/Main/Main';
import Left from './components/left/left';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';

const net = require("./services/network");

const list = [Picture];

const LeftList =


  function LeftList(props) {
    return (
      <div className='leftlist'>
        <Paper elevation={4}>
          <Typography variant="headline" component="h3">
            复杂场景下的在线人体监测系统
        </Typography>
          <Typography component="p">
            v1.0.0
        </Typography>
        </Paper>
        <Divider />
        <List component='nav'>
          <ListItem button onClick={props.callback[0]}>
            <ListItemText primary="图片分析" />
          </ListItem>
          <ListItem button onClick={props.callback[1]}>
            <ListItemText primary="视频分析" />
          </ListItem>
          <ListItem button onClick={props.callback[2]}>
            <ListItemText primary="用户管理" />
          </ListItem>
          <ListItem button onClick={props.callback[3]}>
            <ListItemText primary="模型管理" />
          </ListItem>
        </List>
      </div>
    );
  }



class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      hasLogin: false,
      loging: false,
      registering: true,
      slide: false,
      current: 0
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
  };

  goToLogin = () => {
    this.setState({
      registering: false,
      loging: true
    })
  };

  goToRegister = () => {
    this.setState({
      registering: true,
      loging: false
    })
  };

  LoginCallback = () => {
    this.setState({
      hasLogin: true,
      loging: false,
      registering: false
    })
  };

  registerCallback = () => {
    this.setState({
      registering: false,
      loging: true
    })
  };

  triggerSlide = () => {
    this.setState({
      slide: !this.state.slide
    });
  };

  goToPicture = () => {
    this.setState({
      current: 1
    });
  }

  goToVideo = () => {
    this.setState({
      current: 2
    });
  }

  goToUser = () => {
    this.setState({
      current: 3
    });
  }

  goToModel = () => {
    this.setState({
      current: 4
    });
  }

  render() {
    let navFuncs = [
      this.goToPicture,
      this.goToVideo,
      this.goToUser,
      this.goToModel
    ]
    //注册
    return (
      <div className="all">
        <Header
          logOutHandler={this.logOutHandler}
          menuHandler={this.triggerSlide} />
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
            switch (this.state.current) {
              case 0:
                return <Main />
              case 1:
                return <Picture />
              case 2:
                return <Video />
              case 3:
                return <User />
              case 4:
                return <Model />
            }


          })()}
        </div>
        <div className="footer">
        </div>
        <Left
          listItems={<LeftList callback={navFuncs} />}
          isOpen={this.state.slide}
          troggleFunc={this.triggerSlide}
        />
      </div>
    )
  }
}

export default App;
