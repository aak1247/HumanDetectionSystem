import React, { Component } from 'react';
import "./Main.scss";
import person from "../../images/user.jpg";
import { upload, detect } from "../../services/network";
// import { async } from "../../services/async_network";
import Gravity from '../../components/gravity/gravity';
import Starsky from '../../components/starsky/starsky.js';
import FontAwesome from 'react-fontawesome';



class Main extends Component {
    constructor(props) {
        super(props);
        this.state = {
            imageId: "",
            img: "",
            faces: [],
            detected: false
        }
    }
    detectFaces = () => {
        let formData = new FormData(document.getElementById('uploadForm'))
        let req = upload(formData);
        req.then(res => res.json())
            .then(json => {
                this.setState({
                    imageId: json.id
                });
                return detect(json.id);
            })
            .then(res => res.json())
            .then(json => {
                this.setState({
                    detected: true,
                    img: json.image,
                    faces: json.faces
                })
            }).catch(e => console.error(e));
    }

    render() {
        //主页

        //drawer切换

        return (
            <div className="main">
                <div className="img-detect" onClick={this.detectFaces}>
                    {
                        this.state.detected ?
                            <img src={this.state.img} />
                            : <img src={person} />
                    }
                </div>
                <FontAwesome name="times" />
                <form id="uploadForm"
                    encType="multipart/form-data"
                    action="http://127.0.0.1:5000/detect"
                    method="post">
                    <p>上传</p><input type="file" name="image" />
                    <input type="text" name="name" />
                    <input type="submit" />
                </form>
                <Starsky />
            </div>
        );
    }
}

export default Main;
