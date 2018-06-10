import React, { Component } from 'react';
import "./Main.scss";
import person from "../../images/user.jpg";
import { upload, detect } from "../../services/network";
// import { async } from "../../services/async_network";
import Gravity from '../../components/gravity/gravity';
import Starsky from '../../components/starsky/starsky.js';
import FontAwesome from 'react-fontawesome';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import CardHeader from '@material-ui/core/CardHeader';
import Typography from '@material-ui/core/Typography';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';

    
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

    render() {
        //主页

        //drawer切换

        return (
            <div className="main">
                <GridList cellHeight={360} cols={2}>
                    <GridListTile key='video' cols={1}>
                        <Card size='large'>
                            <CardHeader
                                title="视频分析"
                                subheader="对视频进行分析"
                            />
                            <CardContent>
                                <Typography color="textSecondary">
                                    开始视频分析
                        </Typography>
                                <Typography variant="headline" component="h2">

                                </Typography>
                                <Typography color="textSecondary">

                                </Typography>
                                <Typography component="p">
                                    点击上传视频将视频添加到系统，然后进行分析<br />
                                </Typography>
                            </CardContent>
                            <CardActions>
                                <Button size="small">上传视频</Button>
                                <Button size='small'>查看已检测视频</Button>
                                <Button size='small'>查看分析进度</Button>
                            </CardActions>
                        </Card>
                    </GridListTile>
                    <GridListTile key='picture' cols={1}>

                        <Card size='large'>
                            <CardHeader
                                title="图片分析"
                                subheader="对图片进行分析"
                            />
                            <CardContent>
                                <Typography color="textSecondary">
                                    开始图片分析
                        </Typography>
                                <Typography variant="headline" component="h2">

                                </Typography>
                                <Typography color="textSecondary">

                                </Typography>
                                <Typography component="p">
                                    点击上传图片将视频添加到系统，然后进行分析<br />
                                </Typography>
                            </CardContent>
                            <CardActions>
                                <Button size="small">创建图片库</Button>
                                <Button size='small'>上传图片</Button>
                                <Button size='small'>查看图片库</Button>
                                <Button size='small'>查看分析进度</Button>
                            </CardActions>
                        </Card>
                    </GridListTile>
                    <GridListTile key='user' cols={1}>
                        <Card size='large'>
                            <CardHeader
                                title="用户管理"
                                subheader="管理用户权限"
                            />
                            <CardContent>
                                <Typography color="textSecondary">
                                    开始用户管理
                        </Typography>
                                <Typography variant="headline" component="h2">

                                </Typography>
                                <Typography color="textSecondary">

                                </Typography>
                                <Typography component="p">
                                    点击修改用户权限及其他信息<br />
                                </Typography>
                            </CardContent>
                            <CardActions>
                                <Button size="small">查看所有用户</Button>
                                <Button size='small'>查找用户</Button>
                            </CardActions>
                        </Card>
                    </GridListTile>
                    <GridListTile key='model' cols={1}>
                        <Card size='large'>
                            <CardHeader
                                title="模型管理"
                                subheader="管理模型状态"
                            />
                            <CardContent>
                                <Typography color="textSecondary">
                                    开始模型管理
                        </Typography>
                                <Typography variant="headline" component="h2">

                                </Typography>
                                <Typography color="textSecondary">

                                </Typography>
                                <Typography component="p">
                                    点击进行模型重训练和回滚操作<br />
                                </Typography>
                            </CardContent>
                            <CardActions>
                                <Button size="small">模型重训练</Button>
                                <Button size='small'>模型回滚</Button>
                                <Button size='small'>查看模型状态</Button>
                            </CardActions>
                        </Card>
                    </GridListTile>
                </GridList>

                {/* <div className="img-detect" onClick={this.detectFaces}>
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
                </div> */}
                {/* <form id="uploadForm"
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
                    <input type="text" name="name" />
                </form> */}
                {/* <Starsky /> */}
            </div>
        );
    }
}

export default Main;
