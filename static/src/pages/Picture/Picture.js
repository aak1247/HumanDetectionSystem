import React, { Component } from 'react';
import "./Picture.scss";
import person from "../../images/user.jpg";
import { upload, detect } from "../../services/network";
// import { async } from "../../services/async_network";
import Gravity from '../../components/gravity/gravity';
import Starsky from '../../components/starsky/starsky.js';
import FontAwesome from 'react-fontawesome';
import Button from '@material-ui/core/Button';



class Picture extends Component {
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
                if (json.code == '0') {
                    this.setState({
                        imageId: json.id
                    });
                    return detect(json.id);
                }
                else {
                    return Promise.reject(new Error('upload failed'))
                }
            })
            .then(res => res.json())
            .then(json => {
                if (json.code == '0') {
                    this.setState({
                        detected: true,
                        img: json.image,
                        faces: json.faces
                    })
                }
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
                            <img src={this.state.img} className='detect-img' />
                            : <img src={person} className='detect-img' />
                    }
                    <Button 
                        variant="contained"
                        color="primary"
                        className='uploadButton'
                        onClick={e => {
                            e.stopPropagation();
                            document.getElementById('uploadFile').click();
                        }}>
                        选择图片
                    </Button>
                    <FontAwesome name="times"
                        className='closeModel'
                        onClick={e => {
                            e.stopPropagation();
                            document.getElementsByClassName('detect-img')[0].src = person;
                        }} />
                </div>
                <form id="uploadForm"
                    encType="multipart/form-data"
                    action="http://127.0.0.1:5000/detect"
                    method="post">
                    <p>上传</p>
                    <input type="file"
                        name="image"
                        id='uploadFile'
                        onChange={e => {
                            var reader = new FileReader();
                            reader.readAsDataURL(document.getElementById("uploadFile").files[0]);
                            reader.onload = function (e) {
                                document.getElementsByClassName('detect-img')[0].src = e.target.result;
                            }
                        }} />
                    {/* <input type="text" name="name" /> */}
                </form>
                {/* <Starsky /> */}
            </div>
        );
    }
}

export default Picture;
