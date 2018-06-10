import React, { Component } from 'react';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import CardMedia from '@material-ui/core/CardMedia';
import CardHeader from '@material-ui/core/CardHeader';
import Typography from '@material-ui/core/Typography';

class Video extends Component {
    render() {
        const { classes } = this.props;
        return (
            <div className='video'>
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
                    </CardActions>
                </Card>
            </div>
        );
    }
}

export default Video