import React, { Component } from 'react';
import "./Main.css"
import person from "../../images/person.jpg"




class Main extends Component {
    detect() {
        fetch('http://localhost:5000/detect', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/form-data'
            },
            credentials: 'include',
            body: new FormData(document.getElementById('uploadForm')[0])
        })
        .then(response => response.json())
        .then(function (res) {
            console.log(res)
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
                    action="/detect"
                    method="post">
                        <p>上传</p><input type="file" name="image" />
                    </form>
                </div>
                <div className="footer">
                </div>
            </div>
        );
    }
}

export default Main;
