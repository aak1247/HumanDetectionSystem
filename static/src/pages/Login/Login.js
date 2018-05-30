import React, { Component } from 'react';
import './Login.css'
import { login } from "../../services/network"
import { withStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import FontAwesome from 'react-fontawesome';

const styles = theme => ({
    container: {
        display: 'flex',
        flexWrap: 'wrap',
    },
    textField: {
        marginLeft: theme.spacing.unit,
        marginRight: theme.spacing.unit,
        width: 200,
    },
    menu: {
        width: 200,
    },
    button: {
        margin: theme.spacing.unit,
    },
    input: {
        display: 'none',
    },
});

class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password: "",
            loginFail: false
        }
    }

    handleChange = name => event => {
        this.setState({
            [name]: event.target.value,
        });
    };

    render() {
        const { classes, handleBack, handleNext } = this.props;
        let handleLogin = () => {
            let user = {
                username: this.state.username,
                password: this.state.password
            }
            let res = login(user)
            res.then(
                res => {
                    res.json()
                        .then(
                        json => {
                            if (json.code === 0) {
                                this.setState({
                                    loginFail: false
                                })
                                handleNext()
                            }
                            else {
                                this.setState({
                                    loginFail: true
                                })
                            }
                        })
                }
            ).catch(e => {
                console.log(e)
            })
        }
        return (
            <div className="login">
                <form className={classes.container} noValidate autoComplete="off">
                    <TextField
                        required
                        id="username"
                        label="用户名"
                        className={classes.textField}
                        value={this.state.username}
                        onChange={this.handleChange('username')}
                        margin="normal"
                    />
                    {
                        !this.state.loginFail ?
                            <TextField
                                required
                                id="password-input"
                                label="密码"
                                className={classes.textField}
                                type="password"
                                autoComplete="current-password"
                                margin="normal"
                                onChange={this.handleChange('password')}
                            />
                            :
                            <TextField
                                error
                                id="password-input"
                                label="密码错误"
                                className={classes.textField}
                                type="password"
                                autoComplete="current-password"
                                margin="normal"
                                onChange={(e)=>{
                                    this.setState({loginFail: false})
                                    this.handleChange('password')}}
                            />
                    }
                    <Button variant="raised"
                        className={classes.button}
                        onClick={handleBack}>
                        还没有账号？
                    </Button>
                    <Button variant="raised"
                        color="primary"
                        className={classes.button}
                        onClick={handleLogin}
                    >
                        登录
                    </Button>
                </form>
            </div>
        );
    }
}

export default withStyles(styles)(Login)