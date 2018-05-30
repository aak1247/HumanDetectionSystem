import React, { Component } from 'react';
import { register } from "../../services/network"
import './Register.css'
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

class Register extends Component {
    constructor(props) {
        super(props)
        this.state = {
            username: "",
            password: ""
        }
    }


    handleChange = name => event => {
        this.setState({
            [name]: event.target.value,
        });
    };

    render() {
        const { classes, handleBack, handleNext } = this.props;
        let handleRegister = () => {
            let user = {
                username: this.state.username,
                password: this.state.password
            }
            let res = register(user)
            res.then(
                res => handleNext()
            ).catch(e => {

            })
        }
        return (
            <div className="register">
                <form className={classes.container} noValidate autoComplete="off">
                    <TextField
                        id="username"
                        label="用户名"
                        className={classes.textField}
                        value={this.state.username}
                        onChange={this.handleChange('username')}
                        margin="normal"
                    />

                    <TextField
                        id="password-input"
                        label="密码"
                        className={classes.textField}
                        type="password"
                        autoComplete="current-password"
                        margin="normal"
                        onChange={this.handleChange('password')}
                    />
                    <Button variant="raised"
                        className={classes.button}
                        onClick={handleBack}>
                        已有账号
                    </Button>
                    <Button variant="raised"
                        color="primary"
                        className={classes.button}
                        onClick={handleRegister}
                    >
                        注册
                    </Button>
                </form>
            </div>
        );
    }
}

export default withStyles(styles)(Register)