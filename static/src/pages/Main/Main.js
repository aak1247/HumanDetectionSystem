import React, { Component } from 'react';
import "./Main.css"
import person from "../../images/person.jpg"




class Main extends Component {
    detect() {
        fetch('http://localhost:5000/detect', {
            method: 'POST',
            mode: 'cors',
            // credentials: 'include',
            body: new FormData(document.getElementById('uploadForm'))
        })
        .then(response => console.log(response))
        .then(function (res) {
        console.log(res)
        }).catch(err => {
            debugger
        })
    }
    render() {

        //注册



        //登录



        //主页

        return (
            <div className="main">
                <div className="header">
                    <p>在线人体检测系统</p>
                </div>
                <div className="body">
                    <div className="img-detect" onClick={this.detect}>
                        <img src={person} />
                    </div>
                    <form id="uploadForm"
                        encType="multipart/form-data"
                        action="http://127.0.0.1:5000/detect"
                        method="post">
                        <p>上传</p><input type="file" name="image" />
                        <input type="submit"/>
                    </form>
                </div>
                <div className="footer">
                </div>
            </div>
        );
    }
}

export default Main;
