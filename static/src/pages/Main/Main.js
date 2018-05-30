import React, { Component } from 'react';
import "./Main.css"
import person from "../../images/person.jpg"
import { upload, detect } from "../../services/network"




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
    // detect() {
    //     fetch('http://localhost:5000/detect', {
    //         method: 'POST',
    //         mode: 'cors',
    //         body: new FormData(document.getElementById('uploadForm'))
    //     })
    //         .then(response => console.log(response))
    //         .then(function (res) {
    //             console.log(res)
    //         }).catch(err => {
    //             debugger
    //         })
    // }
    detectFaces = () => {
        let formData = new FormData(document.getElementById('uploadForm'))
        let req = upload(formData);
        req
            .then(
            res => {
                res.json()
                    .then(
                    json => {
                        let imageId = json.id;
                        this.setState({imageId: imageId})
                        let req2 = detect(imageId);
                        req2
                            .then(
                            res2 => {
                                res2.json()
                                    .then(
                                    json2 => {
                                        this.setState({
                                            detected: true,
                                            img: json2.image,
                                            faces: json2.faces
                                        })
                                    }
                                    )
                            }
                            )
                    }
                    )
            }
            )
    }

    render() {
        //主页

        //drawer切换

        return (
            <div className="main">
                <div className="img-detect" onClick={this.detectFaces}>
                    {
                        this.state.detected?
                        <img src={this.state.img} />
                        :<img src={person} />
                    }
                    
                </div>
                <form id="uploadForm"
                    encType="multipart/form-data"
                    action="http://127.0.0.1:5000/detect"
                    method="post">
                    <p>上传</p><input type="file" name="image" />
                    <input type="text" name="name" />
                    <input type="submit" />
                </form>
            </div>
        );
    }
}

export default Main;
