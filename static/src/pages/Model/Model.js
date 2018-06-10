import React, { Component } from 'react';
import './Model.scss'
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

class Model extends Component {
    render() {
        return (
            <div className='model'>
                <Paper elevation={4}>
                    <Typography variant="headline" component="h3">
                        模型管理
                    </Typography>
                    <Typography component="p">
                        <span>模型状态:</span><h3>空闲中</h3>
                    </Typography>
                    <Typography component="p">
                        <span>当前待分析任务数:</span><h3>0</h3>
                    </Typography>
                    <Typography component="p">
                        <span>预计完成时长:</span><h3>0</h3>
                    </Typography>
                    <Typography component="p">
                        <Button variant="raised"
                            color="primary"
                        >
                            重新训练
                        </Button>
                        <Button variant="raised"
                            color="primary"
                        >
                            回滚至
                    </Button>
                    </Typography>
                </Paper>
            </div>
        );
    }
}

export default Model